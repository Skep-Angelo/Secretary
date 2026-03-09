a = ['1', '1']
print(a)

for i in a:
    a[a.index(i)] = int(i)

print(a)