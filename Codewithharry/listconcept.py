list1=["Harry", "rakhi",8,9]

print(list1)
print(list1[2])

#methods of list

num1=[9,34,21,23]
num1.sort()
num1.reverse()


print(num1)

print(num1[1:6:-2]) # thats why we suggest to take only -1 .Not take any others number. We only take -2 or others number when we have only default numbers in slicing

print(len(list1))
list2=[3,9,19,23]
print(max(list2))
print(min(list2))

#To add a number at the end
list2.append(7)
print(list2)


#insert function
list2.insert(0,5)
print(list2)

#remove function
list2.remove(23)
print(list2)

#pop function

list2.pop()
print(list2)
