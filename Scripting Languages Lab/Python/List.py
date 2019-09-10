
list1=[1,2,3,4]
list2=[6,7,8]
list3=[]

def add(list1,list2):
    list3=list1+list2
    print(list3)
def rev(list1):
    list3=list1.reverse()
    print(list1)
    return list3
def revadd(list1):
    list3=list1[::-1]+list1
    print(list3)
add(list1,list2)
rev(list1)
revadd(list1)
