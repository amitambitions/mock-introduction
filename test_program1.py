from program1 import sum

if sum(10, 10) == 20:
    print("Success.")
else:
    print("Failure.")

if sum(0, 1) == 1:
    print("Success.")
else:
    print("Failure.")

if sum(-1, 1) == 0:
    print("Success.")
else:
    print("Failure.")

if sum(12345, 99999) == 112344:
    print("Success.")
else:
    print("Failure.")
