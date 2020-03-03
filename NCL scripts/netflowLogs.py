#How many different IP addresses were recorded
fo = open("netflow.txt", "r")
IPlist = []
for line in fo:
    IP = line[43:63]
    if ( IP not in IPlist):
        IPlist.append(IP)
print(len(IPlist))
    
