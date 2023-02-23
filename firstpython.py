#Counting lists with dictionary key, value pairs.=

a = dict()
c = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for x in c:
    a[x] = a.get(x, 0) + 1
print(a)
