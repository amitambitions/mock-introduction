from a import A

from mock import patch

x = A()
print(x.foo())


def new_foo(self):
    return "New foo"


with patch.object(A, 'foo', new_foo):
    y = A()
    if y.foo() == "New foo":
        print("Success!")
