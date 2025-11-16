# Exercice 6.2 Liste des extensions

def searchext(l):
    """
    Identifie les extensions de la liste de fichiers passÃ©e en argument

    Args:
        l : liste des noms de fichier sous forme de chaine de caractÃ¨res

    Returns:
        Liste des extensions sous forme de chaine de caractÃ¨res
        
    >>> l = searchext(['ARJ.PIF', 'atiogl.xml', 'ativpsrm.bin', 'bfsvc.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['pif', 'xml', 'bin', 'exe']

    >>> l = searchext(['HelpPane.exe', 'hh.exe', 'HPMProp.INI', 'IE9_main.log'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['exe', 'exe', 'ini', 'log']

    >>> l = searchext(['win.ini', 'WindowsShell', 'WindowsUpdate.log', 'winhelp.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['ini', 'log', 'exe']

    >>> l = searchext(['Gfxv2_0.exe.config', 'pstask.dll', 'GfxValDisplayLog.bin'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['config', 'dll', 'bin']
    """
    
    # une list comprehension e des extensions sous forme de chaine de caractÃ¨res
    e = []
    for fic in l:
        res = fic.split(".")
        if len(res) > 1:
            e.append(res[len(res)-1].lower())
    return e
l = ['HelpPane.exe', 'hh.exe', 'HPMProp.INI', 'IE9_main.log']
print(searchext(l))