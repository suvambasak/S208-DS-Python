

def fact(n: int) -> int:
    # pass

    if n < 0:
        return None
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
