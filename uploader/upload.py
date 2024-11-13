import time
import os
import sys

try:
    os.system(".\\upload.bat " + "\"" + sys.argv[2] + ".mp4\"")
except Exception as e:
    print(e)

finally:
    











