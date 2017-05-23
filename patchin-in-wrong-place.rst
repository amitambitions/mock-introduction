

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

