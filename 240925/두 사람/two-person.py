alist = input().split()
blist = input().split()

a_age = int(alist[0])
b_age = int(blist[0])

if (a_age >= 19 and alist[1] == 'M') or (b_age >= 19 and blist[1] == 'F'):
    print(1)
else:
    print(0)