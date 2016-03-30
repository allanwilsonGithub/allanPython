#usr/bin/env python

import unittest

class Test_Windows_Setup(unittest.TestCase):
    def test_hard_disk_space(self):
        import wmi

        c = wmi.WMI ()
        for d in c.Win32_LogicalDisk():
            if d.DriveType == 3:
                drive_type = "Local Disk"
            elif d.DriveType == 2:
                drive_type = "USB"
            elif d.DriveType == 5:
                drive_type = "CD Rom"
            else:
                drive_type = "Unexpected Drive Type"
            print ("Drive Letter: %s, Diskspace %s %s, Drive Type: %s" %(d.Caption, (d.FreeSpace/1024), d.Size, drive_type))
            self.assertIsNotNone(d)


if __name__ == '__main__':
    unittest.main()