value = [1,2,3,4]
a = ""
if isinstance(value, list):
    for i in value:
        a += str(i)
print(int(a))