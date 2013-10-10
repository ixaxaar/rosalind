#! /usr/bin/env python

import sys

def main():
    compliment = {
        'A'     : 'T',
        'T'     : 'A',
        'C'     : 'G',
        'G'     : 'C'
    }

    dna = sys.argv[1]
    rev_cmp = ''
    for base in dna:
        rev_cmp = rev_cmp + compliment[base]

    rev_cmp = bytearray(rev_cmp)
    rev_cmp.reverse()
    print rev_cmp

if __name__ == "__main__":
    main()