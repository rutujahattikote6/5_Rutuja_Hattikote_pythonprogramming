list1=[1,2,"Hello",3.4,"shruti"]
print(type(list1))
print(list1[0: ])
print(list1[ : ])
print(list1[2:4])
print(list1[ :3])
print(list1[0:4:3])
print(list1[-1])
print(list1[-3:-1])

#update list
list1[2]=10
print("\nUpdated list - ",list1)
list1[2:4]=[50,20]
print(list1)

#Repitition
list2=list1*2
print("\nRepeat list - \n",list2)

#concatenation
list3=list1+list2
print("\nconcat list - \n",list3)
print("\nLength of list -",len(list3))

#iterating
for list in list3 :
    print(list)

#membership
print(2 in list1)

#add element in list
list4=[]
n=int(input("\nEnter no of element : "))
for i in range(0,n):
    list4.append(input("\nEnter Element : "))
print(list4)
print("\nlength of list4 - ",len(list4))
print("\nMin of list4 - ",min(list4))
print("\nMax of list4 - ",max(list4))

#remove
list5=[1,2,9,3,4,5]
print("\nbefore remove - ")
print(list5)
list5.remove(9)
print("\nAfter remove list - \n",list5)