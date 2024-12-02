import os

def schedule_task(task_name, script_path, start_date, start_time):
    os.system("..\\res\\scheduler.bat " + task_name + " " + script_path + " " + start_date + " " + start_time)