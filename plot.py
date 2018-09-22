import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from datetime import datetime, timedelta

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

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

fig, ax = plt.subplots()
ax.plot(dates,pages)
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

plt.ylabel('PDF pages')
fig.autofmt_xdate()


fig.savefig('temp.png')
