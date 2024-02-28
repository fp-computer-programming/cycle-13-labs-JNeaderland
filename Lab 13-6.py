my_file = open("alma.txt", "r")
while True:
    line = my_file.readline()
    if len(line) == 0:
        break
    print (line, "\n")
my_file.close