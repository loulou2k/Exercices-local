def lychrel(n):
    """Retourne le nombre d'itÃ©rations nÃ©cessaires pour obtenir un nombre palindrome

    Args:
        n (int): nombre entier soumis au processus de Lychrel

    Returns:
        int: le nombre d'itÃ©rations nÃ©cessaires pour obtenir un nombre palindrome

    >>> n = 50
    >>> lychrel(n)
    1
    >>> n = 55
    >>> lychrel(n)
    2
    >>> n = 59
    >>> lychrel(n)
    3
    >>> n = 69
    >>> lychrel(n)
    4
    >>> n = 79
    >>> lychrel(n)
    6
    >>> n = 89
    >>> lychrel(n)
    24
    >>> n = 107
    >>> lychrel(n)
    1
    >>> n = 108
    >>> lychrel(n)
    1
    >>> n = 109
    >>> lychrel(n)
    2
    """


    cpy=n
    cpy=str(cpy)
    cpy=cpy[::-1]
    cpy=int(cpy)
    res=n + cpy
    res=str(res)
    k = 1
    while(res != res[::-1]):
        k +=1
        n=int(res)
        cpy=n
        cpy=str(cpy)
        cpy=cpy[::-1]
        cpy=int(cpy)
        res=n + cpy
        res=str(res)

    return k

def main():
    # liste de nombres suspectÃ©s d'Ãªtre des nombres de Lychrel
    x = [196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986]
    l = [ lychrel(i) for i in range(1,200) if i not in x ]
    print(l)
    print(lychrel(1186060307891929990))
    pass

if __name__ == "__main__":
    main()