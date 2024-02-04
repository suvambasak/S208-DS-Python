
def fibonacci(n: int) -> int:
    '''
    Parameters
    ----------
    n: int
        n-th term

    Returns
    ---------
    int 
        calculated n-th term
    '''

    if n < 0:
        return None
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
