a,b = map(int, input().split())
ob_hour = 240
i = 0
I = 1
o_hour = ob_hour - b
while i < a:
    if (5*I) < o_hour:
        o_hour -= 5*I
        I += 1
        i += 1
    elif (5*I) == o_hour:
        o_hour -= 5 * I
        i += 1
        break
    elif (5*I) > o_hour:
        break
print(i)
