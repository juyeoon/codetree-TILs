a, b, c = map(int, input().split())
print(1 if min(a,min(b,c)) == a else 0, end = " ")
print(1 if a == b and b == c else 0)