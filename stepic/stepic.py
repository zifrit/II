a = int(input())
b = a%60
c = a-b*60
print(b, c)

n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)
