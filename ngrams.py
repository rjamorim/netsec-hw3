# Network Security Spring 2015 Assignment 3
# Programming problem
# Roberto Amorim - rja2139

from operator import itemgetter
import string, argparse, os

# Here I take care of the command line arguments
parser = argparse.ArgumentParser(description='Extracts strings from a binary file and analizes their ngrams.', add_help=True)
parser.add_argument('-n', dest='n', required=False, type=int, default=3, help='ngram length, default = 3')
parser.add_argument('-s', dest='s', required=False, type=int, default=1, help='Sliding window, default = 1')
parser.add_argument('-i', dest='input', required=True, help='Input file')
#parser.add_argument('-o', dest='output', required=True, help='Output file')
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

# output = args.output

def strings(filename):
    with open(filename, "rb") as f:
        # The file is read one byte at a time, and not loaded in memory
        b = f.read(1)
        result = ""
        while b:
            if b in string.printable:
                result += b
                b = f.read(1)
                continue
            if len(result) >= MINSTRING:
                yield result
            result = ""
            b = f.read(1)

def ngram(input_list, n):
    for string in input_list:
        values = []
        # All the ngram generation code in a single, really hard to understand line. Cheers!
        values.append([string[i:i+n] for i in range(0, len(string)-n+s, s)])
        yield values

strs = list(strings(input))

ngrams = ngram(strs, n)

for i in ngrams:
    print i