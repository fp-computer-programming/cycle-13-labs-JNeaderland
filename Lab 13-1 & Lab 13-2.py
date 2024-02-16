row = {"Naz":12, "John":13, "Jacob":10, "Alsir":15, "Peter":14}
print (row)
#It would keep the key the same but update the value of the key
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