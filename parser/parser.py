''' how to run
make sure that the log data is in the same dir as the script and ____MAKE SURE IT IS CALLED sample_log.txt ____
run the script from cmd or terminal, eg: python script.py 

Code by: Mohammed
written with Python 3.5
'''


import re
from statistics import median
old_rates = []
new_rates = []
times = []
f = open("sample_log.txt", 'r')
lines = f.readlines()
f.close()
i = 0
for line in lines:
    if "not active" in line:
        pass
    else:
        regex = r'''\d+\.+\w{3}'''
        matches = re.findall(regex, line)
        time = line[0:24]
        old =float( matches[1])
        new = float( matches[2])

        old_rates.append(old)
        new_rates.append(new)
        times.append(time)

maxN = max(new_rates)
minN = min(new_rates)
avgN = sum(new_rates) / len(new_rates)
middleN = median(new_rates)

maxO = max(old_rates)
minO = min(old_rates)
avgO = sum(old_rates)/len(old_rates)
middleO = median(old_rates)
print(" New Rates Info: ")
print("The maximum new rate in MBps is: " + str(maxN)+ ", happend at: " + times[new_rates.index(maxN)])
print("The minimum new rate in MBps is: " + str(minN)+ ", happend at: " + times[new_rates.index(minN)])
print("The average new rate in MBps is: " + str(avgN))
print("The median new rate in MBps is: " + str(middleN))
print("Note that the avarage is calculated by summing all new rates and divided by thier total count")
print("Also, note that the median 'middle' in case the rates count is odd will be the middle value, eg: 1,2,3 will give 2. But if the rates count is even then median 'middle' is calculated by taking the average of the two middle values")

print(" \n \n Old Rates Info: ")
print("The maximum old rate in MBps is: " + str(maxO)+ ", happend at: " + times[old_rates.index(maxO)])
print("The minimum old rate in MBps is: " + str(minO)+ ", happend at: " + times[old_rates.index(minO)])
print("The average old rate in MBps is: " + str(avgO))
print("The median old rate in MBps is: " + str(middleO))
print("Note that the avarage is calculated by summing all old rates and divided by thier total count")
print("Also, note that the median 'middle' in case the rates count is odd will be the middle value, eg: 1,2,3 will give 2. But if the rates count is even then median 'middle' is calculated by taking the average of the two middle values")