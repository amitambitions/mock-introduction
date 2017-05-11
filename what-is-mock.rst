What is Mock?
=============

The term "mock" is used both as a noun and a verb when it comes to unit-testing. As a developer, when you
are writing software, you write a companion code that test's the original piece of code that you'd written. This
second piece of code is written in such as way that it is usually less-complex that the original, uses the original
an uses human-planted values to check the original piece of code.

For e.g, if our task is to write a program that does a sum of two numbers, we will write

a) Program that does a sum of two numbers.

b) A test program that verifies that the program written is correct, by using some values that we calculate using
pen-and paper.

Let's write our program first.

**program1.py**

.. include:: program1.py


Before writing the test program, we determine what we expect from our program.

Here are my expectations.

10 + 10 = 20

0  + 1  = 1

-1 + 1  = 0

12345 + 99999 =  112344


So, I will write my test program like this.


.. include:: test_program1.py



