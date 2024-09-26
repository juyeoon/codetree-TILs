cnt = 0

for _ in range(3):
    ilist = input().split()
    if ilist[0] == 'Y' and int(ilist[1]) >= 37:
        cnt += 1

print('E' if cnt >= 2 else 'N')