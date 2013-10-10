#! /usr/bin/env python

from __future__ import division
import sys

# TODO: solve this problem in a better way
# genes = {
# 		'homo_dominant':	'XX',
# 		'mixed_dominant':	'Xx',
# 		'homo_recessive':	'xx'
# }

# def select_first_gen(pop):

def main():
	# pop = {
	# 	'homo_dominant':	sys.argv[1],
	# 	'mixed_dominant':	sys.argv[3],
	# 	'homo_recessive':	sys.argv[2]
	# }

	pop = sys.argv[1:len(sys.argv)]

	total_pop = ctr = 0

	for p in pop:
		total_pop = total_pop + int(p)
		pop[ctr] = int(p)
		ctr = ctr + 1

	select_one_homo_dominant = ((pop[0])/total_pop)
	select_one_mixed_dominant = ((pop[1])/total_pop)
	select_one_homo_recessive = ((pop[2])/total_pop)

	select_one_homo_dominant_iter2x = ((pop[0])/(total_pop - 1))
	select_one_mixed_dominant_iter2x = ((pop[1])/(total_pop - 1))
	select_one_homo_recessive_iter2x = ((pop[2])/(total_pop - 1))

	select_one_homo_dominant_iter2 = ((pop[0] - 1)/(total_pop - 1))
	select_one_mixed_dominant_iter2 = ((pop[1] - 1)/(total_pop - 1))
	select_one_homo_recessive_iter2 = ((pop[2] - 1)/(total_pop - 1))

	expression = select_one_homo_dominant * select_one_homo_dominant_iter2 \
	+ select_one_homo_dominant * select_one_homo_recessive_iter2x \
	+ select_one_homo_recessive * select_one_homo_dominant_iter2x \
	+ select_one_homo_dominant * select_one_mixed_dominant_iter2x \
	+ select_one_mixed_dominant * select_one_homo_dominant_iter2x \
	+ select_one_mixed_dominant * select_one_mixed_dominant_iter2 * (3/4) \
	+ select_one_homo_recessive * select_one_mixed_dominant_iter2x * (2/4) \
	+ select_one_mixed_dominant * select_one_homo_recessive_iter2x * (2/4)

	print round(expression, 5)
	print expression


if __name__ == "__main__":
    main()
