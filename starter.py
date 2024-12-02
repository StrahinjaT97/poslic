import sys
import os
import random as rn
from datetime import datetime as dt
from datetime import timedelta
import subprocess as sp

from common.scheduler import schedule_task






# Schelude itself
def schedule_self():
    
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

def call_scripts():
    files = []

    for (dirpath, dirname, filenames) in os.walk(".\\site viewers\\"):
        t = (dirpath, filenames)
        files.append(t)

    for f in files:
        if len(f) > 1:
            for j in f[1]:
                if ".py" in j:
                    script_name = f[0] + j
                    print("Calling: " + script_name)
                    driver_path = os.getcwd() + "\\res\\chromedriver.exe"
                    sp.Popen(['python', script_name, driver_path, "https://www.svenskhockey.tv/sv/content/u16-regional", "soskicilija@hotmail.com",  "Il!ja064"])

# schedule_self() #TODO: Otkomentarisati 

# Call other scripts
call_scripts()



