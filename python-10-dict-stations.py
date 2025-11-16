# vos import ici...
import csv
from collections import namedtuple
FILENAME = 'meteo-france-stations.csv'

def build_stations_dict(csvfile):
    """
    retourne un dictionnaire des stations mÃ©tÃ©o du fichier passÃ© en argument

    Args:
        csvfile: un fichier au format csv contenant une liste de stations mÃ©tÃ©o

    Returns:
        dictionnaire de namedtuple des informations relatives aux stations mÃ©tÃ©o
        
    >>> d = build_stations_dict(FILENAME)
    >>> print(d['NICE'])
    Station(ID='07690', Latitude=43.648833, Longitude=7.209, Altitude=2)
    >>> print(d['BELLE ILE-LE TALUT'])
    Station(ID='07207', Latitude=47.294333, Longitude=-3.218333, Altitude=34)
    >>> print(d['CAYENNE-MATOURY'])
    Station(ID='81405', Latitude=4.822333, Longitude=-52.365333, Altitude=4)
    >>> print(d['NICE'].Latitude)
    43.648833
    """
    # votre code ici...
    d = dict()
    Station = namedtuple('Station', ['ID', 'Latitude', 'Longitude', 'Altitude'])

    with open(FILENAME, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for ligne in reader:
            for val in ligne.values():
                val = val.split(";")
                d[val[1]] = Station(val[0], float(val[2]), float(val[3]), int(val[4]))
    return d

def main():
    d = build_stations_dict(FILENAME)
    print(d['NICE'])
    pass

if __name__ == '__main__':
    main()