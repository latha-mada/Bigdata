#!/usr/bin/python

import os
import sys
import subprocess
#sys_path = os.path.abspath(__file__)
# sys_path = os.path.join(os.path.abspath(__file__), os.pardir)
sys_path = os.path.dirname(os.path.abspath(__file__))
print(sys_path)
sys.path.append(sys_path)
raw_file_path = os.path.join(sys_path, 'nfl_data')
cmd = 'ls {}'.format(raw_file_path)
print(cmd)
proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()
print(out)
# do backup
if out:
	file1 = os.path.join(raw_file_path, out.splitlines()[0])
	print file1
	in_path = os.path.join(sys_path, 'input')
	print in_path
	mv_cmd = 'mv {} {}'.format(file1,in_path)
	print(mv_cmd)
	proc = subprocess.Popen(mv_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = proc.communicate()
	print(out)
else:
	print("no files to transfer")
