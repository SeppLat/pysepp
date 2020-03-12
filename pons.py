import re
from urllib.request import *
from json import JSONDecoder

def dicts(lang):
    langs = []
    for lang in JSONDecoder().decode(urlopen('https://api.pons.com/v1/dictionaries?language={}'.format(lang)).read().decode('utf-8')):
        lang.pop('directed_label', None)
        langs.append(lang)
    return langs

_subs = [
            ['<.+?>', ''],
            ['\\\\u200a', ' '],
            ['  ', ' '],
        ]

def raw_translations(pons_dict, src_word, pons_secret):
    req = Request('https://api.pons.com/v1/dictionary?q={}&l={}'.format(src_word, pons_dict))
    req.add_header('X-Secret', pons_secret)
    t = urlopen(req).read().decode('utf-8')
    for sub in _subs:
        t = re.sub(sub[0], sub[1], t)
    return t

def _parse_content(translations, content):
    for t in content:
        if 'type' in t and t['type'] == 'entry':
            _parse_content(translations, t['roms'][0]['arabs'][0]['translations'])
        if 'target' in t and len(t['target']) > 0:
            translations.append(t)

def translations(pons_dict, src_word, pons_secret):
    content = raw_translations(pons_dict, src_word, pons_secret)
    content = JSONDecoder().decode(content)[0]['hits']
    translations = []
    _parse_content(translations, content)
    return translations
