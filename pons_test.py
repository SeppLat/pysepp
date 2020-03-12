#!/usr/bin/python3

import pons
from sys import argv, exit
from pprint import pprint
from json import JSONDecoder

if len(argv) < 2:
    print("Usage: ./pons_test.py [pons secret]")
    exit(-1)

def __test(title, result):
    print('\n\n--{}--\n\n'.format(title))
    pprint(result)

def dicts(lang):
    __test('DICTS ({})'.format(lang), pons.dicts(lang))

def translations(pons_dict, word):
    __test(word, pons.translations(pons_dict, word, argv[1]))

def raw(pons_dict, word, decoded_and_pretty):
    raw = pons.raw_translations(pons_dict, word, argv[1])
    if decoded_and_pretty:
        raw = JSONDecoder().decode(raw)
    __test('{} (RAW)'.format(word), raw)

def run_tests():
    dicts('de')
    translations('dela', 'arcere')
    translations('dela', 'nonnumquam')
    translations('dela', 'vir')
    raw('dela', 'nonnumquam', True)

def main():
    run_tests()

if __name__ == '__main__':
    main()
