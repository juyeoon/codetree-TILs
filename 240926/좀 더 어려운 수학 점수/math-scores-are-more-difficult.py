a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a[0] == b[0]:
    print('A' if a[1] > b[1] else 'B')
else:
    print('A' if a[0] > b[0] else 'B')