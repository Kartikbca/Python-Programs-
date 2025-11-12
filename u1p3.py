a = bytearray([1,2,3,4,5])

for i in range(0,len(a)):
    print(a[i])

#modify
for i in range(0,len(a)):
    a[i] += 5

print("After modify:")
for i in range(0,len(a)):
    print(a[i])
