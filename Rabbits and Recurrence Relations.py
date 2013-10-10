#! /usr/bin/env python

import sys

def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    pop_n1 = 1
    pop_n2 = 1
    pop = 0

    for ctr in range(n-2):
        pop = pop_n1 + k*pop_n2
        pop_n2 = pop_n1
        pop_n1 = pop

    print pop

if __name__ == "__main__":
    main()
