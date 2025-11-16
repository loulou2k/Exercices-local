def est_premier(n):
    prem=True
    val = int(input("donner une valeur : "))

    for i in range(2,(val//2 +1)):
        if(val%i == 0):
            prem=False
            break
    return prem
