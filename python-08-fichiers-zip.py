# Vos import ici...
import zipfile

ARCHIVE = 'meteofrance2014.zip'

def extract_temp(date, code):
    """
    retourne la liste des tempÃ©ratures pour la date et la station mÃ©tÃ©o passÃ©es en arguments 

    Args:
        date: une date au format AAAAMMJJ
        code: code de la station mÃ©tÃ©o

    Returns:
        liste des tempÃ©ratures en degrÃ©s Celsius
        
    >>> print(extract_temp('20140109', '07005')) # Abbeville le 9 janvier 2014
    [11.2, 11.6, 11.8, 11.0, 9.6, 8.2, 7.9, 6.8]
    >>> print(extract_temp('20140317', '07110')) # Brest le 17 mars
    [7.2, 7.3, 7.2, 7.5, 8.7, 9.8, 8.5, 7.9]
    >>> print(extract_temp('20140623', '07434')) # Limoges le 23 juin 2014
    [20.2, 17.0, 16.1, 16.1, 18.2, 17.6, 16.3, 15.0]
    >>> print(extract_temp('20140815', '07761')) # Ajaccio le 15 aout 2014
    [18.2, 16.7, 17.8, 25.8, 25.5, 24.9, 22.5, 19.4]
    >>> print(extract_temp('20140703', '89642')) # Terre AdÃ©lie le 3 juillet 2014
    [-17.7, -19.2, -18.7, -19.6, -20.4, -20.8, -23.3, -23.3]
    >>> print(extract_temp('20140703', '12345')) # Station inconnue
    []
    >>> print(extract_temp('20150703', '89642')) # date non comprise dans l'archive
    []
    """
    file_zip = []
    temps = []
    with zipfile.ZipFile(ARCHIVE, "r") as zipf:
        file_zip = zipf.namelist()
        for file in file_zip :
            contenu = []
            if date[0:6] == file.split(".")[1]:
                with zipf.open(file) as f:
                    for ligne in f:
                        val = ligne.decode("utf-8").strip().split(";")
                        val.append(ligne)
                        contenu.append(val)
                for ligne in contenu :
                    if ligne[0] == code and ligne[1][0:8] == date :
                        temps.append(round(float(ligne[7]) - 273.15, 1))

    return temps
    
def main():
    # ... votre code de test ici
    #print(extract_temp('20140703', '12345'))
    print(extract_temp('20140703', '89642'))
    pass

if __name__ == '__main__':
    main()