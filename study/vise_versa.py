inputList = []

with open('dataset_24465_4.txt') as inf:
    for line in inf:
        inputList += line.splitlines()

with open('answer_7.txt','w') as out:
    for line in range(len(inputList)-1,0,-1):
        out.write(inputList[line]+'\n')