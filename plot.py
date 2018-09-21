import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from datetime import datetime, timedelta

with open("data-pages","r") as f:
    for line in f:
        pages = line.split(",")
        pages = [float(i) for i in pages]

with open("data-days","r") as f:
    for line in f:
        days = line.split(",")
        days = [float(i) for i in days]

d = datetime(2018, 9, 18)
dates = [(d - timedelta(days=i)) for i in reversed(days)]
#dates = (datetime.strptime(i, "%Y-%m-%d") for i in dates)
# dates = (datetime.strftime(i, "%m-%d-%Y") for i in dates)

fig = plt.figure()
plt.plot(dates,pages)
plt.ylabel('PDF pages')
plt.xlabel('Date')
fig.savefig('temp.png')
