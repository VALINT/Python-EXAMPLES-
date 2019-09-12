def update_dictionary(d, key, value):
    if(key in d):
        d[key] += [value]
    elif(key*2 in d):
        d[key*2] += [value]
    else:
        d.get(key*2)
        d[key*2] = [value]

d = {}
print(d)
update_dictionary(d,1,2)
print(d)
update_dictionary(d,3,4)
print(d)
update_dictionary(d,1,3)
print(d)
update_dictionary(d,2,8)
print(d)
update_dictionary(d,5,8)
print(d)
update_dictionary(d,2,1)
print(d)
update_dictionary(d,3,0)
print(d)