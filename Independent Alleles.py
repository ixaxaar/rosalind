#!/usr/bin/env python

from __future__ import division
from scipy.misc import comb
import sys

def main():
	# One interesting thing to this problem is the probability of any
	# parent producing an offspring with AaBb alleles is 1/4
	k = int(sys.argv[1])
	N = int(sys.argv[2])
	res = 0

	# for N or more children
	for n in range(N, 2**k + 1):
		# pCr * p1^n * (1-p1)^(p-n)
		res += comb(2**k, n)*((1/4)**n)*((1 - 1/4)**(2**k - n))

	print res


if __name__ == "__main__":
    main()

