#! /usr/bin/env python

from __future__ import division
import sys

def main():
    #    FASTA file
    fasta = open(sys.argv[1], 'r')
    seq = base = name = greatest_name = ''
    gc = greatest_gc = total = float(0)

    line = fasta.readline()
    while (line != ''):
        if line[0] == '>':
            # Compute the GC levels
            for base in seq:
                if (base == 'C' or base == 'G'): gc = gc + 1
                total = total + 1

            
            if total > 0 and (gc/total) > greatest_gc:
                greatest_gc = gc/total
                greatest_name = name

            name = line
            seq = ''
            gc = total = 0
        else:
            seq += line.rstrip()

        line = fasta.readline()

    for base in seq:
        if (base == 'C' or base == 'G'): gc = gc + 1
        total = total + 1

    if total > 0 and (gc/total) > greatest_gc:
        greatest_gc = gc/total
        greatest_name = name

    greatest_name = greatest_name[1:len(greatest_name)]
    greatest_gc = round(greatest_gc*100, 6)
    print greatest_name
    print greatest_gc


if __name__ == "__main__":
    main()
