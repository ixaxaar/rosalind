#! /usr/bin/env python

import sys

codon_table = '''
UUU F
CUU L
AUU I
GUU V
UUC F
CUC L
AUC I
GUC V
UUA L
CUA L
AUA I
GUA V
UUG L
CUG L
AUG M
GUG V
UCU S
CCU P
ACU T
GCU A
UCC S
CCC P
ACC T
GCC A
UCA S
CCA P
ACA T
GCA A
UCG S
CCG P
ACG T
GCG A
UAU Y
CAU H
AAU N
GAU D
UAC Y
CAC H
AAC N
GAC D
UAA Stop
CAA Q
AAA K
GAA E
UAG Stop
CAG Q
AAG K
GAG E
UGU C
CGU R
AGU S
GGU G
UGC C
CGC R
AGC S
GGC G
UGA Stop
CGA R
AGA R
GGA G
UGG W
CGG R
AGG R
GGG G
'''

codon_table_array = codon_table.split('\n')
codon_table_dict = {}
peptide_table_dict = {}

for a in codon_table_array:
	if (a): codon_table_dict[a.split(' ')[0].strip()] = a.split(' ')[1].strip()

for a in codon_table_array:
	if(a): 
		try:
			peptide_table_dict[a.split(' ')[1].strip()] += 1
		except KeyError:
			peptide_table_dict[a.split(' ')[1].strip()] = 1

base = 1000000

def main():
	protein = sys.argv[1]
	solution = peptide_table_dict['Stop']	# 3 possible stop codons
	# mods = 0

	for peptide in protein:
		solution *= peptide_table_dict[peptide]
		if(solution >= base):
			# mods += 1
			solution = solution % base

	print solution


if __name__ == "__main__":
    main()
