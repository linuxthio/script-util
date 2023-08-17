import os
import sys


pack = ""
for i in range(1, len(sys.argv)):
    pack += " " + sys.argv[i]


def pip(pack):
    s = f"pip install {pack} --break-system-packages"
    os.system(s)


pip(pack)
