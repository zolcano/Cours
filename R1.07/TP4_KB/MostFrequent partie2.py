L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

x = max(L1)
b = [-1, -1]
while x != -1:
    a = L1.count(x)
    if a > b[0]:
        b[0] = a
        b[1] = x
    x -= 1

print("Le nombre le plus frequent dans la liste est le :",b[1],"(",b[0]," x)")
