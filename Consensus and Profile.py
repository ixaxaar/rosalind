#! /usr/bin/env python

import sys
import pandas as pd
import itertools

def main():

	fasta = open(sys.argv[1], 'r')
	dim = 1000

	profile = {
		'A': [0]*dim,
		'C': [0]*dim,
		'G': [0]*dim,
		'T': [0]*dim
	}

	cur_seq = ''
	line = fasta.readline()
	while(line != ''):
		if (line[0] == '>'):
			if (cur_seq):
				ctr = 0
				for base in cur_seq:
					profile[base][ctr] += 1
					ctr += 1
				cur_seq = ''
		else:
			cur_seq += line.rstrip()

		line = fasta.readline()

	ctr = 0
	for base in cur_seq:
		profile[base][ctr] += 1
		ctr += 1
	cur_seq = ''

	consensus = ''
	for ctr in range(dim):
		m = max(profile['A'][ctr], profile['C'][ctr], profile['T'][ctr], profile['G'][ctr])
		if (profile['A'][ctr] == profile['C'][ctr] == profile['T'][ctr] == profile['G'][ctr] == m): 
			consensus += ''
			profile['A'][ctr] = profile['C'][ctr] = profile['T'][ctr] = profile['G'][ctr] = ''
		elif profile['A'][ctr] == m: consensus += 'A'
		elif profile['C'][ctr] == m: consensus += 'C'
		elif profile['T'][ctr] == m: consensus += 'T'
		elif profile['G'][ctr] == m: consensus += 'G'


	out = open('out', 'w')		
	out.write(consensus)
	out.write(pd.DataFrame(profile).transpose().to_string())


if __name__ == "__main__":
    main()
