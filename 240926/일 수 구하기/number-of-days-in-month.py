n = int(input())

day31 = [1,3,5,7,8,10,12]

if n == 2:
    print(28)
elif n in day31:
    print(31)
else:
    print(30)