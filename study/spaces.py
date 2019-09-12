# this function find way to the needed spacename
def find(lst, parent):                                          
    tempLstKeys = lst.keys()
    if(parent in lst):
        return [parent]
    else:
        for key in lst.keys():
            temp = find(lst[key][0],parent)
            if(temp != 'None'):
                return [key] + temp
    return('None')

# this function create new namespace inside existed namespace, both names takes to input from keyboard
def create(lst, namespace, parent, keys = ['global']):
    tempDict = {namespace:[{},[]]}
    tempLst = lst.keys()
    tempKeys = find(lst,parent)
    if(parent in lst):
        lst[parent][0].update(tempDict)
    else:
        for key in tempKeys:
            if(len(tempKeys) > 1):
                tempKeys.remove(key)
                create(lst[key][0],namespace,parent,tempKeys)
                break

#this function create nem object(variable) in existed namespace, both names takes to input from keyboard
def add(lst, namespace, var, keys = ['global']):
    tempLst = lst.keys()
    tempKeys = find(lst,namespace)
    if(namespace in lst):
        lst[namespace][1] += [var]
    else:
        for key in tempKeys:
            if(len(tempKeys) > 1):
                tempKeys.remove(key)
                add(lst[key][0], namespace, var ,tempKeys)
                break

# this function searches object(variable) inside needed namespace, if in needed namespace variable didn`t searched
# function searches object with same name in parents namespaces till goes to "global" namespace
def get(lst, namespace, var, keys = ['global']):
    tempLst = lst.keys()
    tempKeys = find(lst,namespace)
    print(tempKeys)
    for key in tempKeys:
            if(len(tempKeys) > 1):
                tempKeys.remove(key)
                ret = get(lst[key][0], namespace, var ,tempKeys)
                if(ret != 'None'):
                    return ret 
                elif(var in lst[key][1]):
                    return key
                else:
                    return 'None'
            else:
                if(var in lst[key][1]):
                    return namespace
                else:
                    return 'None'

# this function recognize and executes commands needed for user
def spaces(lst, comand, namespace, var_par):
    if(comand == 'create'):
        create(lst, namespace, var_par)
    elif(comand == 'add'):
        add(lst, namespace, var_par)
    elif(comand == 'get'):
        print(get(lst, namespace, var_par))
    else:
        print('Ti sho ebobo, protry your eyes, Dodik!')

# main part
spacesDict = {'global':[{},[]]}

comandsAmount = int(input())

for i in range(comandsAmount):
    comandList = input().split(' ')
    spaces(spacesDict,*comandList)