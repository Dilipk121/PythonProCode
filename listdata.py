list1 = [12,"twelve",34.65,True,'C']

print(type(list1))

print(list1)

print(list1[0:100])

print(list1[2:])
print(list1[:20])

print(list1 + list1)
print(list1 * 3)

#here you can re assign value to any assigmed list data, same can not possible in tuple
list1[0] = 100

print(list1[0])

# here it will gives error, bcoz index 6 is not assigned thats why "assigment out of range error"
#list1[6]=121
#print(list1[6])
