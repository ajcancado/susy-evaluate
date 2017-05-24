#!/usr/bin/python

import sys
from shutil import copyfile

copyfile(sys.argv[1], 'output.txt')