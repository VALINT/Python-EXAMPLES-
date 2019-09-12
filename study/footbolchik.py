teamsAmount = int(input())
teamsDict = {}
inputStr = []

for i in range(0,teamsAmount):
    inputStr = input().split(';')
    for j in range(0,4,2):
        tempDict = {}
        if(inputStr[j] in teamsDict):
            tempDict = teamsDict[inputStr[j]]
            tempDict['games'] += 1
            tempDict['wins'] += int(inputStr[j+1] > inputStr[j-1])
            tempDict['draws'] += int(inputStr[j+1] == inputStr[j-1])
            tempDict['loses'] += int(inputStr[j+1] < inputStr[j-1])
            teamsDict[inputStr[j]] = tempDict
        else:
            tempDict.get('games')
            tempDict.get('wins')
            tempDict.get('draws')
            tempDict.get('loses')
            #tempDict.get(inputStr[j]+'_scores')
            tempDict['games'] = int(1)
            tempDict['wins'] = int(inputStr[j+1] > inputStr[j-1])
            tempDict['draws'] = int(inputStr[j+1] == inputStr[j-1])
            tempDict['loses'] = int(inputStr[j+1] < inputStr[j-1])
            teamsDict[inputStr[j]] = tempDict
inputStr = teamsDict.keys()
print(inputStr)

for i in teamsDict:
    print(i,':',teamsDict[i]['games'],teamsDict[i]['wins'],teamsDict[i]['draws'],teamsDict[i]['loses'],str(int(teamsDict[i]['wins'])*3+int(teamsDict[i]['draws'])))