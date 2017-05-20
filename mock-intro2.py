from mock import patch

with patch.object(A, 'foo') as mock_foo:
    mock_foo.return_value = "New Foo"

    y = A()
    if y.bar() == "New foo":
        print("Success!")
