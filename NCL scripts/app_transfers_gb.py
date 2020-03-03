#How many total gigabytes of data was transferred in this log?
#NOT WORKING
fo = open("app_transfers.log", "r")
transferList = []
GBlist = []
totalGB = 0

for line in fo:
    if "\"transfered\":" in line:
        transferList.append(line)
        
for line in transferList:
    if "KB" in line:
        num = line[17:21].strip()
        if " KB" in num:
            num = num[0]
            print(num)
        num = float(num) / 8192
        GBlist.append(num)
        
    elif "MB" in line:
        num = line[17:21].strip()
        if " MB" in num:
            num = num[0]
            print(num)
        num = float(num) / 1024
        GBlist.append(num)
        
for i in GBlist:
    totalGB += i
print(totalGB)

