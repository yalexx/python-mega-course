import os
import time

import pandas

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean())
    else:
        print("File does not exist")
    time.sleep(10)
