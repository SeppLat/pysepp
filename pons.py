from os import system
from urllib.request import urlopen

def get_pons_dicts(lang):
    res = urlopen('https://api.pons.com/v1/dictionaries?language={}'.format(lang))
    return res.read()

def get_pons_translations():
    return
