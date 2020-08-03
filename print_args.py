#!/usr/bin/python3

import sys

nb_args = len(sys.argv) - 1
print("Je suis {} et j'ai reçu {} arguments :"
      .format(sys.argv[0], nb_args))
for i in range(1, nb_args + 1):
    print("    - argument {}: '{}'".format(i, sys.argv[i]))
