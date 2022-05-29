import operator

examdatabase = {}
count = 0

for r in range(10):
    name,score = input("Enter name and score: ").split()
    k = name
    examdatabase[k] = float(score)
    count += 1

print("--------------------")
print("Sorted student data:")


for k in sorted(examdatabase.keys()):
    print(k,"\t %.2f" %examdatabase[k])

print("--------------------")

highestscore = max(examdatabase.items(), key=operator.itemgetter(1))[1]
minscore = min(examdatabase.items(), key=operator.itemgetter(1))[1]


highest_key = []
minest_key = []
for person, score in examdatabase.items():
    if score == highestscore:
        highest_key.append((person, score))
    elif score == minscore:
        minest_key.append((person, score))

pairri = 0

for pair in highest_key:
    if pairri < 1:
        print("Student(s) with max score of %.2f:"% (pair[1]),end = " ")  
        pairri += 1
    print(pair[0],end = " ")

print()


pairi = 0
for pair in sorted(minest_key): 
    if pairi < 1:
        print("Student(s) with min score of %.2f:"% (pair[1]),end = " ")
        pairi += 1
    print(pair[0],end = " ")

print()

average = 0
print("Student(s) who passes the exam >= 50.00:",end = " ")
for k in sorted(examdatabase.keys()):
    average = average + examdatabase[k]
    if examdatabase[k] >= 50:
        print(k, end = " ")

average = average / 10
print()
print("Student(s) who scored at least and above average score of %.2f:"% average,end = " ")
for k in sorted(examdatabase.keys()):
    if examdatabase[k] >= average:
        print(k, end = " ")

print()
print("--------------------")

loop = True
while loop:
    inpt = input("Enter your query name: ")
    if inpt == "Quit" or inpt == "qUit" or inpt == "quIt" or inpt == "quiT" or inpt == "QUit" or inpt == "qUIt" or inpt == "quit" or inpt == "QUIT" or len(inpt) < 1 or len(inpt) > 20:
        print("Bye")
        loop = False
        exit()
    elif inpt in examdatabase:
        print("Score of",inpt,"is %.2f" % examdatabase[inpt])
        if examdatabase[inpt] < 50:
            print("%s has NOT passed the exam."%inpt)
        else:
            print("%s has PASSED the exam."%inpt)
    else:
        print("%s is not in the database." % inpt)