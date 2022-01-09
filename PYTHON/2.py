sin = 0
afr = 0
ind = 0
rai = 0
pal = 0
git = 0
smmv = 908526
logro = 0
a = 0
b = 0
c = 0
val = int(input())
for i in range(1, val+1):
    var_1 = input().lower()
    var_2 = int(input())
    var_3 = int(input())
    if var_1 == "sin reconocimiento":
        a = 4 * 0
    elif var_1 == "afrodescendiente":
        a = 4 * 12
    elif var_1 == "indigena":
        a = 4 * 15
    elif var_1 == "raizal":
        a = 4 * 18
    elif var_1 == "palenquero":
        a = 4 * 21
    if var_1 == "gitano":
        a = 4 * 24
    
    if var_2 == 1:
        b = 5 * 30
    elif var_2 == 2:
        b = 5 * 24
    elif var_2 == 3:
        b = 5 * 18
    elif var_2 == 4:
        b = 5 * 6
    elif var_2 == 5:
        b = 5 * 0
    elif var_2 == 6:
        b = 5 * 0
    if var_3<smmv:
        c = 6 * 45
    elif var_3 >= smmv and var_3 < smmv*2:
        c = 6 * 27
    elif var_3 >= smmv*2 and var_3 < smmv*4:
        c = 6 * 21
    elif var_3 >= smmv*4 and var_3 < smmv*5:
        c = 6 * 12
    elif var_3 >= smmv*5:
        c = 0 * 6
    
    if ((var_1=="sin reconocimiento") and (var_2 >=1 and var_2<=6) and (var_3>0)):
        sin+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
    elif ((var_1 =="afrodescendiente") and (var_2 >=1 and var_2<=6) and (var_3>0)):
        afr+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
    elif ((var_1 =="indigena") and (var_2 >=1 and var_2<=6) and (var_3>0)):
        ind+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
    elif ((var_1 =="raizal") and (var_2 >=1 and var_2<=6) and (var_3>0)):
        rai+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
    elif ((var_1 =="palenquero") and (var_2 >=1 and var_2<=6) and (var_3>0)):
        pal+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
    elif ((var_1 =="gitano") and (var_2 >=1 and var_2<=6) and (var_3>0)):
        git+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
        
    a = 0
    b = 0
    c = 0
    
print(f"{logro}\nsin reconocimiento {sin}\nafrodescendiente {afr}\nindigena {ind}\nraizal {rai}\npalenquero {pal}\ngitano {git}")