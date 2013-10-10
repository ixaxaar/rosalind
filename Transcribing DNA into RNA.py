#! /usr/bin/env python

import sys

def main():
    dna = sys.argv[1]
    rna = ''
    for base in dna:
        rna = rna + (((base == 'T') and 'U') or base)

    print rna

if __name__ == "__main__":
    main()
