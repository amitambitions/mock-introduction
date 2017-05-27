Unittest module
===============

The simple test example.

::

    import unittest

    class SimplisticTest(unittest.TestCase):

        def test(self):
            self.failUnless(True)

    if __name__ == '__main__':
        unittest.main()


Running this will the output like this.

::

    $ python unittest1.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
