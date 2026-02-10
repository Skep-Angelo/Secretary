a = [1,2, [list(range(1,4))]]
time = []
for i in a:
    if isinstance(i, list):
        time.append(i[0])
    else:
        time.append(i)



