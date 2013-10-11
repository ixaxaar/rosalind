#! /usr/bin/env python

from __future__ import division
import sys

dominance = {
    'AA_AA':	1,
    'AA_Aa':	1,
    'AA_aa':	1,
    'Aa_Aa':	(3/4),
    'Aa_aa':	(2/4),
    'aa_aa':	0
}

def main():
	population = {
	'AA_AA':	sys.argv[1],
    'AA_Aa':	sys.argv[2],
    'AA_aa':	sys.argv[3],
    'Aa_Aa':	sys.argv[4],
    'Aa_aa':	sys.argv[5],
    'aa_aa':	sys.argv[6]
	}

	offspring = 0

	for d in dominance:
		offspring += dominance[d]*float(population[d])

	# each couple produces 2 offsprings
	print offspring*2


if __name__ == "__main__":
    main()
