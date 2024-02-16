tt=int(input("minutes :"))
m = tt%60
h = tt%60
j= h//24
M = j//31
print(M,"mois",j,"jour.s",h,"heure.s",m,"minute.s")
