#usr/bin/env python

import subprocess

def get_host_stats():
    ''' This function just runs the "df -h" command and returns the output'''
    df = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    output = df.communicate()[0]
    return output

host_stats = get_host_stats()
print host_stats