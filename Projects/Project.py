arr = []
arr2 = [1, 2, 1, 2, 1, 2, 1, 2, 1]
flag = 0


num = int(input("enter your id: "))
temp = num
counter = 0
while temp != 0:
    counter += 1
    temp //= 10
for x in 9 - counter:
    arr[x] = 0
temp = num
for x in counter:
     arr[x + (9 - counter)] = temp 

"""
000012345
121212121
"""
        
