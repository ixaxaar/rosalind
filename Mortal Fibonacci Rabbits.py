#! /usr/bin/env python

import sys

def main():
	timespan = int(sys.argv[1])
	lifespan = int(sys.argv[2])
	maturity = 1

	ctr = 0
	pop = [1, 1, 1] # Hack to acheive the result, as the death-rate progresses this way

	while(ctr < timespan - 2):
		l = 0 # no of bunnies that die
		
		if ((len(pop) - lifespan) > 0):
			l = pop[-lifespan - 1]
		else: l = 0

		pop.append(pop[-1] + pop[-2] - l)

		ctr = ctr + 1

	print pop


if __name__ == "__main__":
    main()
