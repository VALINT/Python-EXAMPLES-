string = ''
lst = []

with open('dataset_3363_2.txt') as inf:
    for line in inf:
        line = line.strip()
        for i in range(0,len(line)):
            if(line[i] > '9'):
                string += ' ' + line[i]+' '
            else:
                string += line[i]
        lst = string.split()

string = ''

for i in range(0,len(lst),2):
    string += (lst[i]*(int(lst[i+1])))
print(string)
            