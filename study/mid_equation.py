#this function is filling dictionare, were key is word an data is number of this words in text
def words_amount(d, lst):                               
    d.get(str(lst[0]))
    d[lst[0]] = lst[1],lst[2],lst[3]

dictionary = {}
lst = []
outStr = ''
midVal = int(0)
midRus = int(0)
midPhi = int(0)
midMat = int(0)

with open('dataset_3363_4.txt') as inf:
    for line in inf:
        line = line.strip()
        lst = line.split(';')
        for i in range(0, len(lst)):
            words_amount(dictionary,lst)

with open('answer_4.txt','w') as out:
    for i in dictionary:
        midRus += int(dictionary[i][0])
        midPhi += int(dictionary[i][1])
        midMat += int(dictionary[i][2])

        midVal = (int(dictionary[i][0]) + int(dictionary[i][1]) + int(dictionary[i][2]))/3
        out.write(str(midVal)+'\n')
    midRus = midRus/(len(dictionary.keys()))
    midPhi = midPhi/(len(dictionary.keys()))
    midMat = midMat/(len(dictionary.keys()))
    out.write(str(midRus)+' '+str(midPhi)+' '+str(midMat))