tup = (45,56,78,48,12,56,48,989,56,313,45,458,465,321,89,465,65,28,48,465,4655,3211)

even = []
odd = []

for i in tup :
    if (i % 2 == 0) :
        even.append(i)
    else:
        odd.append(i)

print("Even Numbers ", even)
print("Odd Numvers ", odd)