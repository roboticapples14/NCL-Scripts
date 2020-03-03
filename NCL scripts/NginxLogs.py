#How many different IP addresses reached the server sucessfully
#Code "400"
fo = open("access.log", "r")
IPlist = []
for line in fo:
    IP = line[:13]
    if ( IP not in IPlist):
        IPlist.append(IP)
print(len(IPlist))
    
