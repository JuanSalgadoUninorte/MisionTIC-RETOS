sin = afr = ind = rai = pal = git = 0
smmv = 908526
no_paso = logro = error = 0
a = b = c = 0
val = int(input())
for i in range(1, val+1):
    entrada = input().split(",")
    var_a,var_b,var_c=str(entrada[0]),int(entrada[1]),int(entrada[2])
    var_1 = var_a.lower()
    var_2 = int(var_b)
    var_3 = int(var_c)
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
        #cambio de backend de variable
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
    #cambio de backend de variable
    if var_3<smmv:
        c = 6 * 45
    elif smmv<=var_3< smmv*2:
        c = 6 * 27
    elif smmv*2<=var_3< smmv*4:
        c = 6 * 21
    elif smmv*4<=var_3< smmv*5:
        c = 6 * 12
    elif var_3 >= smmv*5:
        c = 0 * 6
    
    if ((var_1=="sin reconocimiento") and (6>=var_2>= 1) and (var_3>0)):
        sin+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
        else:
            no_paso+=1
    elif ((var_1 =="afrodescendiente") and (6>=var_2>= 1) and (var_3>0)):
        afr+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
        else:
            no_paso+=1
    elif ((var_1 =="indigena") and (6>=var_2>= 1) and (var_3>0)):
        ind+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
        else:
            no_paso+=1
    elif ((var_1 =="raizal") and (6>=var_2>= 1) and (var_3>0)):
        rai+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
        else:
            no_paso+=1
    elif ((var_1 =="palenquero") and (6>=var_2>= 1) and (var_3>0)):
        pal+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
        else:
            no_paso+=1
    elif ((var_1 =="gitano") and (6>=var_2>= 1) and (var_3>0)):
        git+=1
        d = (a + b + c) / 15
        if d >= 20:
            logro+=1
        else:
            no_paso+=1
    else:
        error+=1
    a = 0
    b = 0
    c = 0
planta = [
    ["sin reconocimiento",sin],
    ["afrodescendiente",afr],
    ["indigena",ind],
    ["raizal",rai],
    ["palenquero",pal],
    ["gitano",git]]
planta = sorted(planta, key=lambda x: (x[1], x[0]), reverse=True)
print(f"{logro} {no_paso} {error}")
for i in range(6):
    print(planta[i][0],"",planta[i][1])