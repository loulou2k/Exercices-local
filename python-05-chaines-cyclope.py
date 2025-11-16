def is_cyclope(n):
    """retourne la vÃ©ritÃ© de "n est un nombre cyclope"

    Args:
        n (int): nombre Ã  tester

    Returns:
        bool: True si "n est un nombre cyclope". False sinon
    
    >>> n = 1230456
    >>> is_cyclope(n)
    True
    >>> n = 1237456
    >>> is_cyclope(n)
    False
    >>> n = 120056
    >>> is_cyclope(n)
    False
    """
    n=str(n)
    zero=False
    imp=False
    if((len(n) % 2) != 0):
        imp=True
        pos=len(n)//2
        if(n[pos] == "0"):
            zero=True
    
    if(imp and zero):
        return True
    else:
        return False

def main():
    print(is_cyclope(1230456))
    print(is_cyclope(1237456))
    print(is_cyclope(120056))
    pass

if __name__ == "__main__":
    main()