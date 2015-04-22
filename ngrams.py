# Network Security Spring 2015 Assignment 3
# Programming problem
# Roberto Amorim - rja2139

import operator
import itertools
import argparse
import os

# Here I take care of the command line arguments
parser = argparse.ArgumentParser(description='Extracts strings from a binary file and analizes their ngrams.', add_help=True)
parser.add_argument('-n', dest='n', required=False, type=int, default=3, help='ngram length, default = 3')
parser.add_argument('-s', dest='s', required=False, type=int, default=1, help='Sliding window, default = 1')
parser.add_argument('-i', dest='input', required=True, help='Input file')
parser.add_argument('-o', dest='output', required=True, help='Output file')
args = parser.parse_args()

# Configuration variables
MINSTRING = 4

n = int(args.n)
if n < 1 or n > 3:
    print "ERROR: The ngram length is outside the acceptable range! (1-3)"
    exit(1)

s = int(args.s)
if s < 1:
    print "ERROR: The sliding windows length is outside the acceptable range! (>1)"
    exit(1)

if not os.path.isfile(args.input):
    print "ERROR: Invalid file name for analysis"
    exit(1)
else:
    input = args.input

output = args.output

# The function that extracts ngrams from the list of strings
def ngram(filename, n, s):
    with open(filename, "rb") as f:
        line = f.readline()
        values = []
        while line:
            # All the ngram generation code in a single, really hard to understand line. Cheers!
            values.append([line[i:i+n] for i in range(0, len(line)-n+s, s)])
            line = f.readline()
        f.close()
        yield values


counted = []
def most_common(L):
    sortedlist = sorted((x, i) for i, x in enumerate(L))
    groups = itertools.groupby(sortedlist, key=operator.itemgetter(0))
    # auxiliary function to get "quality" for an item
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(L)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        #print 'item %r, count %r, minind %r' % (item, count, min_index)
        counted.append([item, count])
        return count, -min_index
    # pick the highest-count/earliest item
    return max(groups, key=_auxfun)[0]

ngrams = ngram(input, n, s)

# Flattening the ngram list
chain = itertools.chain.from_iterable(ngrams)
chain2 = itertools.chain.from_iterable(chain)

most_common(list(chain2))
sort = sorted(counted, key=operator.itemgetter(1), reverse=True)

file = open(output, "wb")
for i in range (0,20):
    file.write(str(i + 1) + ":  " + " ".join(hex(ord(n)) for n in sort[i][0]) + ", count: " + str(sort[i][1]) + "\n")
file.close()

