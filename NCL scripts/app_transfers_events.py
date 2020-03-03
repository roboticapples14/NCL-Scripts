#Which day saw the largest number of events?	
fo = open("app_transfers.log", "r")
tsList = []
for line in fo:
    if "\"ts\":" in line:
        tsList.append(line)
dateLi = []
for line in tsList:
    date = line[9:19]
    dateLi.append(date)
ten = 0
eleven = 0
twelve = 0
el = 0
for line in dateLi:
    if "2019-02-10" in line:
        ten += 1
    elif "2019-02-11" in line:
        eleven += 1
    elif "2019-02-12" in line:
        twelve += 1
    else:
        el += 1
print("2019-02-10:", ten)
print("2019-02-11:", eleven)
print("2019-02-12:", twelve)
print("other:", el)

    
        
