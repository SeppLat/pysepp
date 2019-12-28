from os import system
from urllib.request import *
from json import JSONDecoder, JSONEncoder

def get_pons_dicts(lang):
    return urlopen('https://api.pons.com/v1/dictionaries?language={}'.format(lang)).read().decode('utf-8')

def get_pons_translations(pons_dict, src_word, pons_secret):
    req = Request('https://api.pons.com/v1/dictionary?q={}&l={}'.format(src_word, pons_dict))
    req.add_header('X-Secret', pons_secret)
    content = urlopen(req).read().decode('utf-8')
    content = JSONDecoder().decode(content)[0]['hits'][0]['roms'][0]
    word = content['headword']
    word_full = content['headword_full']
    translations = []
    for a in content['arabs']:
        for t in a['translations']:
            translations.append(t)
    return translations
