#! /usr/bin/env python

from itertools import izip
import sys


def translate(seq):
    bases = ['u', 'c', 'a', 'g']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))

    seq = seq.lower().replace('\n', '').replace(' ', '')
    peptide = ''
    
    for i in xrange(0, len(seq), 3):
        codon = seq[i: i+3]
        amino_acid = codon_table.get(codon, '*')
        if amino_acid != '*':
            peptide += amino_acid
        else:
            break
                
    return peptide

def grouped(iterable, n):
    return izip(*[iter(iterable)]*n)

def main():
    seq = sys.argv[1]

    protein = ''

    for c1, c2, c3 in grouped(seq, 3):
    	protein = protein + translate(c1 + c2 + c3)

    print protein


if __name__ == "__main__":
    main()
