import re
from urllib.request import *
from json import JSONDecoder, JSONEncoder

def get_pons_dicts(lang):
    langs = []
    for lang in JSONDecoder().decode(urlopen('https://api.pons.com/v1/dictionaries?language={}'.format(lang)).read().decode('utf-8')):
        lang.pop('directed_label', None)
        langs.append(lang)
    return langs

def get_pons_translations(pons_dict, src_word, pons_secret):
    req = Request('https://api.pons.com/v1/dictionary?q={}&l={}'.format(src_word, pons_dict))
    req.add_header('X-Secret', pons_secret)
    content = urlopen(req).read().decode('utf-8')
    content = re.sub('<.+?>', '', content)
    content = JSONDecoder().decode(content)[0]['hits'][0]['roms'][0]['arabs']
    translations = []
    for a in content:
        for t in a['translations']:
            if len(t['target']) > 0:
                translations.append(t)
    return translations
