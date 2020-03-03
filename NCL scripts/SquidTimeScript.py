#Get longest request time
fo = open("squid_access.log", "r")
timeList = []
for line in fo:
    time = line[16:22].strip()
    timeList.append(int(time))
    print(time)
Tmax = 0
for i in timeList:
    if (i > Tmax):
        Tmax = i
print(Tmax)
