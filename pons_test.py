#!/usr/bin/python3

from pons import *
from sys import argv, exit
from pprint import pprint

if(len(argv) < 2):
    print("Usage: ./pons_test.py [pons secret]")
    exit(-1)

pprint(get_pons_dicts('de'))
pprint(get_pons_translations('dela', 'arcere', argv[1]))
