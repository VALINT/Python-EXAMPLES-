def graph(dic):
    for keys in list(dic.keys()):
        temp = set()
        for setEls in dic[keys]:
            temp.update(dic[setEls])
        dic[keys].update(temp)

def creates(dic, create, parents = []):
    if(len(parents)  == 0):
        tempDict = {create : set([create])}
        dic.update(tempDict)
    else:
        for objkt in parents:
            if(objkt not in list(dic.keys())):
                tempDict = {objkt : set([objkt])}
                dic.update(tempDict)
        tempDict = {create : set([create])}
        dic.update(tempDict)
        for obj in parents:
            tempSet = set(dic[obj])
            dic[create].update(tempSet)
    graph(dic)

def find(dic, parent, finded):
    if(finded not in list(dic.keys())):
        return 'No'

    tempSet = set(dic[finded])
    
    if(parent in tempSet):
        return 'Yes'
    else:
        return 'No'

 
def commands(dic, create, command = ':', *parents):
    if(command == ':'):
        if(len(parents) == 0):
            creates(dic, create)
        else:
            creates(dic, create, parents)
    else:
        print(find(dic,create,str(command)))

dic = dict()
clasesNum = int(input())

for i in range(clasesNum):
    tempList = input().split(' ')
    if(len(tempList) == 0):
        commands(dic, tempList)
    else:
        commands(dic, *tempList)
        

#S"""  """for key in dic:
#    print(key,' - ',dic[key])

clasesNum = int(input())

for i in range(clasesNum):
    tempList = input().split()
    if(len(tempList) == 0):
        commands(dic, tempList)
    else:
        commands(dic, *tempList)        
    