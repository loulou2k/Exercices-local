# Vos import ici
import string

def check_password(password):
    """
    Teste la robustesse d'un password

    Args:
        password: chaine de caractÃ¨res

    Returns:
        True or False

    >>> check_password('A1213pokl')
    False
    >>> check_password('bAse730onE')
    True
    >>> check_password('asasasasasasasaas')
    False
    >>> check_password('QWERTYqwerty')
    False
    >>> check_password('123456123456')
    False
    >>> check_password('QwErTy911poqqqq')
    True
    """

    # Si la longueur n'est pas conforme, retourner False
    # Si l'un des caractÃ¨res n'est pas un chiffre, retourner False
    # Si l'un des caractÃ¨res n'est pas une lettre minuscule, retourner False
    # Si l'un des caractÃ¨res n'est pas une lettre majuscule, retourner False

    # Q : OÃ¹ puis je trouver l'ensemble des lettres et des chiffres sans le reconstituer moi mÃªme ? 
    # R : Jeter un oeil au module string
    leng=False
    low=False
    up=False
    idig=False
    if (len(password) >= 10):
        leng=True
        for ch in password:
            if ch.isdigit():
                idig=True
            if ch.islower():
                low=True
            if ch.isupper():
                up=True
    if(leng and low and up and idig):
        return True
    else:
        return False

def main():
    # votre code de test ici...
    # Exemple :
    result = check_password('A1213poklaz')
    print(result)
    pass

if __name__ == '__main__':
    main()