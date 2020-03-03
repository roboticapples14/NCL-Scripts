fo = open("access.log", "r")
IPList = []
for line in fo:
    IP = line[:13].strip()
    if IP not in IPList:
        IPList.append(IP)
for i in IPList:
    num = 0
    for j in fo:
        IP = j[:13].strip()
        if IP == i:
            num = num + 1
    print("IP: ", IP, "num: ", num)
        

