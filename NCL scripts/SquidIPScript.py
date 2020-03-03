#How many different IP addresses did the proxy service in this log?
fo = open("squid_access.log", "r")
IPList = []
for line in fo:
    IP = line[22:35].strip()
    IPList.append(IP)
IPList = list( dict.fromkeys(IPList) )
print(len(IPList))


#How many GET requests were made?
GETlist = []
for line in fo:
    if "FOR" in line:
        GETlist.append(line)
        print(line)
    

