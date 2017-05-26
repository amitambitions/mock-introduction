What is Testing
===============

Testing in general programming terms is the practice of writing code (separate from your actual application code)
that invokes the code it tests to help determine if there are any errors.

It does not prove that the code is correct (which is only possible under very restricted circumstances). It merely
reports if the conditions the tester thought are handled correctly.

There are two kinds of errors.

* Syntax Errors
* Logical Errors

The compiler will help with the syntax errors.
In order to verify that our program does not have any logical errors, we write unittests.


Why Testing

* Testing makes sure your code works properly under a given set of conditions.

* Testing assures correctness under a basic set of conditions.

* Testing allows one to ensure that changes to the code did not break existing functionality.


* Writing tests forces you to think about the the code under unusual conditions, possibly revealing logical errors.

* Good testing requires modular, decoupled code, which is a hallmark of good system design.

* The whole practise of unit-testing is made much easier by code that is loosely coupled.

