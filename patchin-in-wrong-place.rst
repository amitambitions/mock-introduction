Let's consider a data source class

::

    # data_source.py
    def get_name():
        return "Alice"


And the Person class exposes a method that fetches data from the data source.

::

    # person.py
    from data_source import get_name

    class Person(object):
        def name(self):
            return get_name()

One might then start to write the test case that looks like this.


::

    # test_person.py
    from mock import patch
    from person import Person

    # mock the get_name function
    @patch('data_source.get_name') # This won't work as expected!
    def test_name(mock_get_name):
        # set a return value for our mock object
        mock_get_name.return_value = "Bob"
        person = Person()
        name = person.name()
        assert name == "Bob"

This will not work because the patch is happening at the data source. Not from the place at which it is imported.


The option is to change the source code.

::


    # person.py
    import data_source

    class Person(object):
        def name(self):
            return data_source.get_name()

Which is generally not a good idea. Although, since we control both the code and tests, we might be able to change
this too.

The other option is to change the test code, and changing the place we patch.

::

    # test_person.py
    from mock import patch
    from person import Person

    # mock the get_name function
    @patch('test_person.get_name')
    def test_name(mock_get_name):
        # set a return value for our mock object
        mock_get_name.return_value = "Bob"
        person = Person()
        name = person.name()
        assert name == "Bob"


Forgetting the patch the return value

We need to patch the object, which is called. Sometimes we patch the class, and expect that method on the patched
object will be return our planted value. This is false. We need to access the instance using the return_value and
access the method and then override it.


::

    # person.py
    class Person(object):
        def __init__(self):
            self.pet = Pet()
        [... other methods ...]

    class Pet(object):
        def noise(self):
            return "Woof"

If the requirement is to patch the noise method. This is the wrong way.


::

    @patch('person.Pet')
    def test_dog_noise(mock_pet):
        mock_pet.noise.return_value = "Meoow"
        person = Person()
        assert person.pet.noise() == "Meoow"

What's wrong?

* mock_pet is a mocked class object. We need to access the instance, which done by calling the class.
* so we need to use mock_pet.return_value.

The correct way to patch this class will be.

::

    @patch('person.Pet')
    def test_dog_noise(mock_pet):
        # Here we need an extra `return_value` attribute in order to access the
        # instance of the class
        mock_pet.return_value.noise.return_value = "Meoow"
        person = Person()
        assert person.pet.noise() == "Meoow"


Patching a decorator
--------------------

The control of decorator needs to be understood. When python interprets a module, the entire module is loaded /
scanned. So mocking the decorator later will not have any effect.

::

    def useless_decorator(func):
        print "Hi, I'm a decorator that does nothing."
        return func

    class Foo(object):
        print "Entering Foo class definition"

        @useless_decorator
        def bar(self):
            return 42

    print "OK, we're done with that class definition."

**function to test**


::

    # person.py
    from decorators import noise_logger

    class Person(object):
        def __init__(self):
            self.pet = Pet()

    class Pet(object):
        @noise_logger
        def noise(self):
            return "Woof"

Here is an attempt to patch the decorator and test it.


::

    from mock import patch
    from person import Person

    @patch('person.noise_logger', lambda x: x)
    def test_decorator():
        person = Person()
        assert person.pet.noise() == "Woof"


This is the wrong way to test since it will be patching at the wrong place.
The decorator is already associated with nose when the class is imported.


The correct way is to patch the decorator before invoking the class itself.


::

    from mock import patch
    patch('decorators.noise_logger', lambda x: x).start()
    from person import Person

    def test_decorator():
        person = Person()
        assert person.pet.noise() == "Woof"

* This takes to declare patch in a separate module.
* Patches the module.
* And calls .start on the patch method.



The start call on mock object, activates the patch.

::

    def start(self):
        """Activate a patch, returning any created mock."""
        result = self.__enter__()
        self._active_patches.append(self)
        return result

