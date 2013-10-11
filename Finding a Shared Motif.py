#! /usr/bin/env python

import sys

# other ways to do it would be using difflib or building sequence trees

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr

def main():
	fasta = open(sys.argv[1], 'r')
	seq = ''
	lines = []

	# read everything from the given file
	line = fasta.readline()
	while(line != ''):
		if (line[0] == '>'):
			if seq != '':
				lines.append(seq)
				seq = ''
		else:
			seq += line.rstrip()

		line = fasta.readline()

	lines.append(seq)

	print long_substr(lines)


if __name__ == "__main__":
    main()

