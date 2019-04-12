num= int(input("enter number: "))

if num == 1:
    print("one")
elif num == 2:
    print("two")
elif num == 3:
    print("three")
elif num == 4:
    print("four")
elif num == 5:
    print("five")
elif num == 6:
    print("six")
elif num == 7:
    print("seven")
elif num == 8:
    print("eight")
elif num == 9:
    print("nine")
elif num > 9 and num < 100:
    sum = num % 10 + num // 10
    print(num, "is 2 digit number, sum is", sum)

elif num > 99 and num < 1000:
    sum = (num % 10) * ((num // 10) % 10) * (num // 100)
    print(num, "is 3 digit number, mul is", sum)
elif num > 999:
    print (num, "has more than 3 digits")
