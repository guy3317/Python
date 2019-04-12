flag = 0

while flag == 0:
    num= int(input("enter number: "))
    temp = num
    opp = 0
    while temp != 0:
        opp *= 10
        opp += temp % 10
        temp //= 10
    if num == opp:
        print("polindrome")
        flag = 1
    else:
        print("not a polindrome")
