list1=['grapes','orange',1,2]
print(type(list1))
print(list1[0])
print(list1[-1])
print(list1[1:3])
list1[0]='cherry'
print(list1)
list1[1:3]='mango',2
print(list1)
list1.insert(2,'apple')
print(list1)
list1.append(5)
print(list1)
list2=[1,2,3]
list1.extend(list2)
print(list1)
list1.remove(2)
print(list1)
list1.pop(1)
print(list1)


