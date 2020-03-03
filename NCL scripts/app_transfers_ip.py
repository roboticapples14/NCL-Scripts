#Which IP address demonstrated suspicious behavior?
#Looking for which IP had most transfers
fo = open("app_transfers.log", "r")
IPList = []
for line in fo:
    if "\"ip\":" in line:
        IP = line[5:14].strip()
        IPList.append(IP)
print(IPList)
