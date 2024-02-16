x = int(input("chiffre 1 :"))
y = int(input("chiffre 2 :"))

print("avant permutation :")
print("x :",x)
print("y :",y)

#x,y = y,x

temp = [x, y]
y = temp[0]
x = temp[1]

print("après permutation :")
print("x :",x)
print("y :",y)