Network Security Spring 2015 Assignment 3
Programming problem
Roberto Amorim - rja2139

The program should be run as:
$ python ngrams.py -n 3 -s 1 -i prog1 -o prog1-3-1.txt
where n is the ngram size, s is the slide size, i is the input file and o is the output file

For each given file, the program extracts ngrams and analyzes their frequency. The 20 most
frequent ngrams are stored in the output file in order of frequency, next to the amount of
times each one appeared in the file.

The program is quite fast. Even running on the largest file (prog1), it takes very few
seconds to execute.