#! /usr/bin/env python

import sys

def main():
	fasta = open(sys.argv[1], 'r')
	order = 3

	cur_seq = ''
	connections = []
	seqs = {}

	# we read the whole file here, bad bad monkey :(
	line = fasta.readline()
	while(line != ''):
		if (line[0] == '>'):
			if(cur_seq): seqs[name] = cur_seq
			name = line[1:].rstrip()
			cur_seq = ''
		else: cur_seq += line.rstrip()
		line = fasta.readline()
		
	if(cur_seq): seqs[name] = cur_seq

	for seq in seqs:
		for seq2 in seqs:
			if (seq != seq2):
				if (seqs[seq][-order:] == seqs[seq2][0:order]):
					if (not([seq, seq2] in connections)):
						connections.append([seq, seq2])
				if (seqs[seq2][-order:] == seqs[seq][0:order]):
					if (not([seq2, seq] in connections)):
						connections.append([seq2, seq])

	for n in connections:
		print ' '.join(n)


if __name__ == "__main__":
    main()
