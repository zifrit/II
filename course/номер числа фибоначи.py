# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/eTYuD/nomier-chisla-fibonachchi/submission

a = int(input())
i = 2
f1 = 1
f2 = 1
while f2 != a:
    if f2 > a:
        print(-1)
        break
    elif a == 1:
        print(1)
        break
    else:
        f1, f2 = f2, f1+f2
        i += 1
if f2 == a:
    print(i)