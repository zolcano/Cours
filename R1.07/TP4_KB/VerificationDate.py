date = str(input("Entrez une date (jjmmaaaa) : "))
l = [int(date[0] + date[1]), int(date[2] + date[3]), int(date[4] + date[5] + date[6] + date[7])]

state = True
if len(date) > 8 or len(date) < 8 or l[1] > 12 or l[1] < 1 or l[0] < 1 or l[0] > 31:
    state = False
if (l[1] == 4 or 6 or 8 or 9 or 11) and (l[0] > 30):
    state = False

if l[1] == 2:
    if l[2]%4 == 0 and l[2]%100 != 0 or l[2]%400 == 0:
        if l[1] > 29:
            state = False
    elif l[2] > 28:
        state = False


#MAIN
txt = str(l[0]) + " "+str(l[1]) + " "+str(l[2])
if state == True:
    print("La date ",txt," est correct")
else:
    print("La date ",txt," est incorrect")