import time

log_file = "D:\ALLUSTORE\\allucloud\\alluCloud2\\alluCloud.log"

def test_allucloud_has_ran_today():
    f = open(log_file,"r")
    lines = f.readlines()
    marker = False
    for line in lines:
        if time.strftime("%Y-%m-%d") in line:
            marker = True
    assert marker