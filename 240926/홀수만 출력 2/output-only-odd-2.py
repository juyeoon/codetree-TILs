b, a = map(int, input().split())

for i in range(b, a-1, -1):
    if i%2:
        print(i, end=" ")