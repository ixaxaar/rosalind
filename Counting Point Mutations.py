#! /usr/bin/env python

import sys

def main():
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    base = ''
    ctr = mutations = 0

    for base in str1:
        if (base != str2[ctr]):
            mutations = mutations + 1
        ctr = ctr + 1

    print mutations

if __name__ == "__main__":
    main()

