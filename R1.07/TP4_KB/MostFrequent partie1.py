L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

def fonction(i, L1):
    count = 0
    y = len(L1)-1
    while y != 0:
        if L1[y] == i:
            count += 1
        y -= 1
    return(count)

b = [-1, -1]
a = max(L1)
while a != -1:
    x = fonction(a, L1)
    if x > b[0]:
        b[0] = x
        b[1] = a
    a -= 1

print("Le nombre le plus frequent dans la liste est le :",b[1],"(",b[0]," x)")