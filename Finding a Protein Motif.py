#! /usr/bin/env python

import sys
import urllib2
import re

# N_glycosylation = 'N[^P](S|T)[^P]' lookahead version:
N_glycosylation = r'(?=(N[^P](S|T)[^P]))'

def main():
	prot_ids = sys.argv[1:]
	uniprot = 'http://www.uniprot.org/uniprot/'
	fastas = {}

	for prot_id in prot_ids:
		prot_fid = urllib2.urlopen(uniprot + prot_id + '.fasta')
		prot_fid.readline()
		line = prot_fid.readline().rstrip()
		fastas[prot_id] = ''
		while(line): 
			fastas[prot_id] += line
			line = prot_fid.readline().rstrip()

	ans = {}
	for fasta in fastas:
		iter = re.finditer(N_glycosylation, fastas[fasta])
		ans[fasta] = []
		for i in iter:
			ans[fasta].append(i.start())

	for fasta in ans:
		print
		print fasta
		s = []
		for a in ans[fasta]:
			sys.stdout.write(str(a + 1))
			sys.stdout.write(' ')
	print


if __name__ == "__main__":
    main()
