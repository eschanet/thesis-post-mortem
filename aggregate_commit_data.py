import glob
import os
import collections

data_days = collections.OrderedDict()
for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
    data_days[day] = [0,0]
data_hours = collections.OrderedDict()
for hour in ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']:
    data_hours[hour] = [0,0]

with open('data-commit-days.txt', 'w') as of:
    listing = glob.glob('data-commit-days-*')
    for filename in listing:
        with open(filename, 'r') as f:
            for line in f:
                print line
                if len(line.split(' ')) > 1:
                    day = line.split(' ')[0]
                    added_lines = float(line.split(' ')[1])
                    removed_lines = float(line.split(' ')[2])
                    if day in data_days:
                        lines = data_days[day]
                        added_lines += lines[0]
                        removed_lines += lines[1]
                    data_days[day] = [added_lines, removed_lines]
    print data_days
    for day, lines in data_days.iteritems():
        of.write("{} {} {}\n".format(day,lines[0],lines[1]))

with open('data-commit-hours.txt', 'w') as of:
    listing = glob.glob('data-commit-hours-*')
    for filename in listing:
        with open(filename, 'r') as f:
            for line in f:
                print line
                if len(line.split(' ')) > 1:
                    day = line.split(' ')[0]
                    added_lines = float(line.split(' ')[1])
                    removed_lines = float(line.split(' ')[2])
                    if day in data_hours:
                        lines = data_hours[day]
                        added_lines += lines[0]
                        removed_lines += lines[1]
                    data_hours[day] = [added_lines, removed_lines]
    print data_hours
    for day, lines in data_hours.iteritems():
        of.write("{} {} {}\n".format(day,lines[0],lines[1]))
