def gradesf():
    gds = []
    gdb = []
    grades = {"Quiz Unit 8":89, "Unit 9 Parametric Equations":86,"Test Unit 8":93, "War Case Study:  Declare your topic":100, "War Case Study:  Executive Branch Research":70, "War Case Study:  Legislative Branch":75, "War Case Study:  Judicial Branch":80, "Indecent Presentation":85, "Final Project Pitches":82, "Indecent Reflection":77, "20524 A Place at the Table Presentation":100}
    print (grades.values())
    for grade in grades:
        print (grade)
    for grad in grades.values():
        if int(grad) >= 70:
            gds.append(grad)
        if int(grad) <= 50:
            gdb.append(grad)
    print (gds)
    print (gdb)

def validate_username (name):
    if len(name) <= 6:
        print ("Try Again")
    else:
        if len(name) > 12:
            print ("Try Again")
        else:
            if name[0].isalpha():
                namer = name [::-1]
                i = 0
                if namer[0] != "123" or "!":
                    print ("Try Again")
                else:
                  for letters in name:
                        if name[i].isalpha():
                            i += 1
                        else: print("Try Again")
            else:
                print ("Try Again")


def add_nums():
    nums = [1, 2, 3, 4, 5]
    usnum = input("What's your number? ")
    pl = 0
    #Goes through every value in the list and adds the converted value of the user input to it
    #Unless its a word instead of a number
    for num in nums:
        try:
            nums[pl] += int(usnum)
        except ValueError:
            print ("Input cannot be converted to a number")
            add_nums()
        pl += 1
    print (nums)



def find_evens(a, b):
    numl = [a, b]
    #Makes it from small to large
    numl.sort()
    even = []
    #Takes the numbers given and adds all even numbers between them to the list "even"
    for num in range(numl[0], numl[1]):
        if num % 2 == 0:
            even.append(num)
    print (even)


def count_a(word):
    wordl = word.lower()
    a= word.find("a")
    i = 0
    while a > -1:
        a = wordl.find("a")
        wordl.lower()
        wordl = wordl[a+1:]
        i = i + 1
    if i <= 0:
        print (0)
    else:
        print (i - 1)


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    print("The factorial of ", num, " is ", fact)
