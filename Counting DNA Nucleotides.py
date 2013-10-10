#! /usr/bin/env python

import sys

def main():
	dna_str = sys.argv[1]

	occurences = {
		'A':	0,
		'C':	0,
		'G':	0,
		'T':	0
	}

	for c in dna_str:
		occurences[c.upper()] = occurences[c.upper()] + 1;

	print str(occurences['A']) + " " + str(occurences['C']) + " " + str(occurences['G']) + " " + str(occurences['T'])

if __name__ == "__main__":
    main()
