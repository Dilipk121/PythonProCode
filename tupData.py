tup = ("apple","mango","pine apple","orange","banana")

for i in range(len(tup)) :
    print(tup[i].upper())


print(range(len(tup)))

print(list(range(len(tup))))

arr = [78,45,8,5,895,654,978,465,98,465,5,321]
even = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
print(even)

print(list(even))
