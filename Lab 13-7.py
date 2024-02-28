my_file = open("alma.txt")
contents = my_file.readlines()
contentsr = contents[::-1]
print (contentsr)
my_file.close()