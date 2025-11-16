import math
def fermat(n):
    return pow(2, (pow(2,n))) + 1

def est_premier(n):
    prem=True
    val = n

    for i in range(2,(val//2 +1)):
        if(val%i == 0):
            prem=False
            break
    return prem


def first_non_prime_fermat():
    val=1
    while(est_premier(fermat(val))):
        val +=1
    
    return fermat(val)

def next_prime(n) :
    while(not est_premier(n)):
        n +=1
    return n


def couple_prime_after(n):
    nprime=next_prime(n)
    while(not est_premier(nprime +2)):
        nprime=next_prime(nprime +1)
    return nprime, nprime+2

def germain_prime_after(n):
    nprime=next_prime(n)
    while(not est_premier(2*nprime +1)):
        nprime = next_prime(nprime +1)
    return nprime, 2*nprime +1

print(est_premier(200087))
#print(germain_prime_after(100000))
