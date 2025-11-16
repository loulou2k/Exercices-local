def is_magic(n):
    """retourne la vÃ©ritÃ© de "n est un nombre magique"

    Args:
        n (int): nombre entier Ã  tester

    Returns:
        bool: True si "n est un nombre magique". False sinon

    
    >>> n = 1089
    >>> is_magic(n)
    True
    >>> n = 8019
    >>> is_magic(n)
    False
    >>> n = 10989
    >>> is_magic(n)
    True
    >>> n = 10898
    >>> is_magic(n)
    False
    >>> n = 109989
    >>> is_magic(n)
    True
    >>> n = 108898
    >>> is_magic(n)
    False
    >>> n = 1099989
    >>> is_magic(n)
    True
    >>> n = 1088898
    >>> is_magic(n)
    False
    >>> n = 10891089
    >>> is_magic(n)
    True
    >>> n = 10981089
    >>> is_magic(n)
    False
    >>> n = 10999989
    >>> is_magic(n)
    True
    >>> n = 10999898
    >>> is_magic(n)
    False
    """
    cpy=str(n*9)
    if(n == int(cpy[::-1])):
        return True
    else:
        return False
    
def next_magic(n):
    while(not is_magic(n+1)):
        n +=1
    return n+1

def main():
    print(is_magic(1089))
    print(is_magic(8019))
    print(is_magic(10989))

    print(next_magic(1000))
    print(next_magic(10000))
    print(next_magic(100000))
    pass

if __name__ == "__main__":
    main()