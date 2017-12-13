#!/usr/bin/python

import sys

current_word = None
current_count = 1
# file = "/Users/gummida/test_reduce"
for line in sys.stdin:
# with open(file, 'r') as f:
#     for line in f:
    word = line.strip().split('#')
    if current_word:
        if word[0] == current_word:
            current_count += int(word[1])
        else:
            print "%s  %d" % (current_word, current_count)
            current_count = 1
    current_word = word[0]

if current_count > 1:
    print "%s  %d" % (current_word, current_count)
