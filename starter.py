import sys
import os

import random as rn
from datetime import datetime as dt
from datetime import timedelta



def schedule_task(task_name, script_path, start_date, start_time):
    os.system(".\\res\\scheduler.bat " + task_name + " " + script_path + " " + start_date + " " + start_time)



#Schelude itself
random_offset_minutes = rn.randint(0, 59)
if random_offset_minutes < 10:
    random_offset_minutes = "0" + str(random_offset_minutes)
else:
    random_offset_minutes = str(random_offset_minutes)

random_offset_seconds = rn.randint(0, 59)
if random_offset_seconds < 10:
    random_offset_seconds = "0" + str(random_offset_seconds)
else:
    random_offset_seconds = str(random_offset_seconds)

tomorrow = dt.today() + timedelta(days=1) #TODO: MOZDA SE DURGACIJE FORMATIRA VREME NA MASINI !!!!!
tomorrow = str(tomorrow)
print(tomorrow)
ymd = tomorrow.split("-")
year = ymd[0]
month = ymd[1]
day = ymd[2].split(" ", 1)[0]
tomorrow = month + "/" + day + "/" + year


schedule_task(sys.argv[0], os.getcwd() + "\\" + sys.argv[0], tomorrow, ("06:" + random_offset_minutes + ":" + random_offset_seconds))




