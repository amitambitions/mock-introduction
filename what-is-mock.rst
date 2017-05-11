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


And when I run that `test_program1.py`, I get the output.

::

    $ python test_program1.py
    Success.
    Success.
    Success.
    Success.


Essentially, I used a new program `test_program1.py` to test the validity of another program `program1.py`.


What's the difference between `program1.py` and `test_program1.py`


program1.py

* defines and implements an algorithm. It defines that the sum of two numbers can be calculated using `+` operator.
The algorithm is give a term 'sum`.

test_program1.py

* It does not define any algorithm.
* It hard-codes the input and expected output.
* The hard-coded value of input and output is a result of our knowledge of the expected behavior for "sum" operation.
* Finally, it uses the "sum" procedure of program1.py. Gives our known input values and verifies that the program
gave the output as desired.


This part of using a program and verifying the correct behavior using another program is called "unit-testing".

We demonstrated unit-testing using a very simple program.

The example we used for demonstration was a very simple one. The process, however, is applicable to any complex
program too.

Let's find out the 10th fibonacci number. We will write the fibonacci sequence starting with 0 and 1.

0 1 1 2 3 5 8 13 21 34 55

* We start the sequence with 0.
* We start our counting of the numbers with 1. That is 1st fibonacci number is 0.

Let's write a program for this.

The general form of the program is, you initialize n1 and n2

n3 = n1 + n2

And then, you set n1 to n2 and n2 to n3 and you go until you reach the limit of 10.

n1 = 0
n2 = 1

limit = 1

while limit < 10:

    n3 = n1 + n2
    n1 = n2
    n2 = n3

return  n1

.. include:: fibonacci1.py
















