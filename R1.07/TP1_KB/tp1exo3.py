def moyenne(j,h,m):
    tt=(j-1)*60*24+h*60+m
    print(tt,"minutes ont été écoulées")

j = int(input("jour du mois :"))
h = int(input("heure :"))
m = int(input("minute :"))
moyenne(j, h, m)
