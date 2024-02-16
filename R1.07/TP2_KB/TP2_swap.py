a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")

#a,b,c = b,c,a

temp = [a, b, c]
a = temp[1]
b = temp[2]
c = temp[0]

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)