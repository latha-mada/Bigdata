#!/usr/bin/python

"""
transfers the data files from output directory to remote vm - hadoop cluster
"""
import time
import pexpect
import os
import subprocess
user = 'vagrant'
machine = 'centos-03'
curr_path = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(curr_path, 'output')
bakup_path = os.path.join(curr_path, 'backup', 'output_bak')
cmd = 'ls {}'.format(in_path)
timeout = time.time() + 60*60
while True:
    if time.time() > timeout:
        print("exiting the execution due to timeout")
        break
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    files = out.splitlines()
    if len(files)>0:
        for file in files:
            file_path = os.path.join(in_path, file)
            print file_path
            out_path = os.path.join('home', '{}'.format(user), 'input')
            print out_path
            scp_cmd = 'scp {} {}@{}:/{}'.format(file_path, user, machine, out_path)
            print scp_cmd
            pexpect.run(scp_cmd)
            # print child.before
            pexpect.run("mv {} {}".format(file_path, bakup_path))
            # child = None
    else:
        print("There are no files to transfer. Will try in a minute")
        time.sleep(60)

