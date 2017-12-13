#!/usr/bin/python
import os
import sys
import subprocess
import time
import re
import datetime
retain_indexes = [1,9,2,4,16,17,19,21,23,28,29,30,31,32,34,35,38,39,45,46,53,54,55,58,66,67,70,71]
retain_list = []
in_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input')
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
bak_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backup', 'input_bak')
cmd = 'ls {}'.format(in_path)
stop = False
count = 0
timeout = time.time() + 60*60
while True:
    if time.time() > timeout:
        print("exiting the process due to timeout")
        break
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    list = out.splitlines()
    if len(list) > 0:
        print(" inside if")
        print list
        # stop = True
        time.sleep(1)
        file_name = list[0]
        season = re.search(r'.*_(.*)\..*', file_name).group(1)
        infile = os.path.join(in_path, file_name)
        outfile = os.path.join(out_path, file_name)
        print infile, outfile
        with open(infile, 'r') as fin, open(outfile, 'w') as fout:
            i = 0
            for line in fin:

                if i == 0:
                    i += 1
                    print line
                    # sys.exit(0)
                    continue
                else:
                    retain_list = [season]
                    # print line
                    fields = line.split(',')
                    if fields[67] =='NA' or fields[66]=='NA' or fields[16]=='NA' or fields[17]=='NA':
                        continue
                    # print("length of fields = {}, {}".format(len(fields), i))
                    i += 1
                    for index in retain_indexes:
                        retain_list.append(fields[index])
                    print(','.join(retain_list))
                    fout.write(','.join(retain_list))
                    fout.write(os.linesep)
        bak_cmd = 'mv {} {}'.format(infile, bak_path)
        backup = subprocess.Popen(bak_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = backup.communicate()
        print("out = {}".format(out))


    else:
        print("input is empty. Will keep polling")
        time.sleep(2)

# print path
