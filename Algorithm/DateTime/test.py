def listTimeToString():
    val = [2026, 1, 1, 6, 0, 0]
    padding = [4, 2, 2, 2, 2, 2]
    for i in range(0, len(val)):
        while len(str(val[i])) < padding[i]:
            val[i] = "0" + str(val[i])
    string = ""
    for j in val:
        string += str(j)
    print(string)

listTimeToString()