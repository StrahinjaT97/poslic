@echo off

Rem %1 - task name $2 - task run %3 - start date %4 - start time
schtasks /create /tn "%1" /tr "python %2" /sc once /sd "%3" /st "%4" /f

echo "Successfully created task %1"
