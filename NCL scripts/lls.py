fo = open("IIS.log", "r")
for line in fo:
    if "#" not in line:
        print(line[len(line) - 5: len(line)])
