
dictionary={'is01':'red' ,'is02':'hat','is03':'house','is04':'home','is05':'display','is06':'alpha'}
dictionary['is08']='pink'
delete=[]
print(dictionary)
for key, value in dictionary.items():
    print(key ," with value",value)
    if value[0]=="h":
        delete.append(key)
print(delete)
for i in delete:
    del dictionary[i]
val = list(dictionary.values())
val.sort()
print(val)
print(dictionary)
