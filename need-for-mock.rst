Need for Mock
-------------

Needing to mock out methods when testing is very common and there are lots of tools to help
you with it in Python. The danger with "monkey patching" classes like this is that if you don't
undo it afterwards then the class has been modified for all other uses throughout your tests.

mock library, which is one of the most popular Python mocking libraries, includes a helper called
"patch" that helps you to safely patch methods or attributes on objects and classes during your tests.


The patch decorator can be used as a context manager or as a test decorator. You can either use it to patch
out with functions yourself, or use it to automatically patch with Mock objects that are very configurable.

.. include:: mock-intro1.py


Mock can handle the patching and unpatching for you automatically.
You could get away without defining the mock function yourself.

.. include:: mock-intro2.py


* http://stackoverflow.com/questions/5036920/mocking-out-methods-on-any-instance-of-a-python-class/5044894#5044894
