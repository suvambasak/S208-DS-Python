
def reverse_string_recursive(text: str) -> str:
    '''
    Parameters
    ----------
    text: str
        input string


    Returns
    ---------
    str 
        reverse of the string text
    '''

    if len(text) <= 1:
        return text
    else:
        return reverse_string_recursive(text[1:]) + text[0]
