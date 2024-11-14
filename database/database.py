import pandas as pd
import csv
import sys
import os

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


