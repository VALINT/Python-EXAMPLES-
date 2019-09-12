students = {}

with open('dataset_3380_5.txt') as inf:
    for line in inf:
        line = line.strip().split('\t')
        if(line[0] not in students):
            students.get(line[0])
            students[line[0]] = [line[2]]
        else:
            students[line[0]] +=[line[2]]

for i in students:
    tempVar = float(0)
    for j in range(0,len(students[i])):
        tempVar += int(students[i][j])
    students[i] = [(tempVar/len(students[i]))]

with open('answer_last.txt','w') as out:
    for i in range(1,12):
        if(str(i) in students):
            out.write(str(i)+' '+str(students[str(i)])+'\n')
        else:
            out.write(str(i)+"-"+'\n')
