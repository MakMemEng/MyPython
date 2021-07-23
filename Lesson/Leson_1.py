for i in range(3):
    for j in range(3):
        print(i,j,sep="-")
# print i-j

for i in range(5):
    if i == 3:
        break
    # if i==3 end roop
    print(i)

for i in range(5):
    if i ==3:
         continue
        # if i==3 skip 
    print(i)

arr = [2,4,6,8,10]
for i in arr:
    print(i)

arr = [2,4,6,8,10]
sum = 0
for i in arr:
    sum += i
print(sum)