import pandas as pd
import csv
import sys
import os
import mysql.connector as mysql

#sys.argv[1] = ime robijevog excel fajlsa
#sys.argv[2] = host
#sys.argv[3] = user
#sys.argv[4] = pass
#sys.argv[5] = database

class DatabaseEntry:
    def __init__(self):
        pass

df = pd.read_excel(sys.argv[1], usecols = "A:C,E:H")
df.to_csv("database.csv", header = False, index = False)

with open("database.csv", newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter = ",")
    for row in reader:
        for s in row:
            pass

os.remove("database.csv")


conn = mysql.connect(host = sys.argv[2], user = sys.argv[3], password = sys.argv[4], database = sys.argv[5])

cursor = conn.cursor()

# sql = "neki sql statement sa %s itd parametrima"
# val = [(x11, x12, ..., x1n), ..., (xm1, xm2, ..., xmn)]
# cursor.executemany(sql, val)
# conn.commit()
