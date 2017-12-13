#!/usr/bin/python

import sys

team = 'NE'
play = 'End of Game'
i = -1
required_list = [0,5,6,8,10,13,14,25,26,27,28]
# file = '/Users/gummida/backup/output_bak/pbp_2014_bak.csv'
# with open(file, 'r') as f:
for line in sys.stdin:
    # for line in f:
    out = []
    i += 1
    word = line.strip('\n').split(',')
    if (word[27] == team or word[28] == team) and word[10] ==play:
        home = word[27]
        away = word[28]
        posscore = word[25]
        defescore = word[26]
        pos = word[5]
        out.append(word[0])
        if word[27] == 'NE':
            out.append('HOME')
        else:
            out.append('AWAY')
        try:
            posscore = int(word[25])
            defscore = int(word[26])
        except:
            continue

        if word[5] == team:
            score = int(word[25]) - int(word[26])
            if score > 0:
                out.append(1)
            else:
                # i += 1
                continue
        else:
            score = int(word[26]) - int(word[25])
            if score > 0:
                out.append(1)
            else:
                # i += 1
                continue

        print "%s%s#%d" % (out[0],out[1], out[2])
