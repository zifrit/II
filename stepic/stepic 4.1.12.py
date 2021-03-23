a = list(map(int, input().split()))
b = a[0]
while a[0] >= a[1]:
    if b == a[1]:
        b = a[1]
        b += 1
    elif b > a[1]:
        b += (a[0]//a[1])
        a[0] = a[0]//a[1]
print(b)