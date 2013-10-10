#! /usr/bin/env python

import sys

class Namespace:
	pass

def main():
	ns = Namespace()
	ns.dna     = sys.argv[1]
	repeat = sys.argv[2]
	positions = []
	cur_pos = 0

	while(1):
		try:
			# index throws an exception when it does not find string :/
			p = ns.dna.index(repeat)
		except ValueError:
			break

		if p:
			positions.append(p + cur_pos + 1) # 1 added for string numbering to start with 1
			cur_pos += p + 1
			ns.dna = ns.dna[p + 1:]
		else: break

	print str(positions)


if __name__ == "__main__":
    main()
