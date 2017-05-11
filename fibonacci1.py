def fibo(limit):
    n1 = 0
    n2 = 1
    idx = 1
    while idx < limit:
        n3 = n1 + n2

        idx += 1
        n1 = n2
        n2 = n3
    return n1
