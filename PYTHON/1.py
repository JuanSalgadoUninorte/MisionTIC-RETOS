var_1 = input("Ingrese su reconocimiento etnico: ").lower()
smmv = 908526
if var_1=="sin reconocimiento":
    valor_1=0
    r_e = 4
    var_2 = int(input("Ingrese el numero de su estrato socioeconmico: "))
    if var_2==1:
        e_s = 5
        valor_2=30
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))    
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==2:
        e_s = 5
        valor_2=24
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==3:
        e_s = 5
        valor_2=18
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==4:
        e_s = 5
        valor_2=6
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==5:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==6:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    else: 
        print("Se presento un error")
elif var_1=="afrodescendiente":
    valor_1=12
    r_e = 4
    var_2 = int(input("Ingrese el numero de su estrato socioeconmico: "))
    if var_2==1:
        e_s = 5
        valor_2=30
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))    
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==2:
        e_s = 5
        valor_2=24
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==3:
        e_s = 5
        valor_2=18
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==4:
        e_s = 5
        valor_2=6
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==5:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==6:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    else: 
        print("Se presento un error")
elif var_1=="indigena":
    valor_1=15
    r_e = 4
    var_2 = int(input("Ingrese el numero de su estrato socioeconmico: "))
    if var_2==1:
        e_s = 5
        valor_2=30
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))    
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==2:
        e_s = 5
        valor_2=24
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==3:
        e_s = 5
        valor_2=18
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==4:
        e_s = 5
        valor_2=6
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==5:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==6:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    else: 
        print("Se presento un error")
elif var_1=="raizal":
    valor_1=18
    r_e = 4
    var_2 = int(input("Ingrese el numero de su estrato socioeconmico: "))
    if var_2==1:
        e_s = 5
        valor_2=30
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))    
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==2:
        e_s = 5
        valor_2=24
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==3:
        e_s = 5
        valor_2=18
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==4:
        e_s = 5
        valor_2=6
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==5:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==6:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    else: 
        print("Se presento un error")
elif var_1=="palenquero":
    valor_1=21
    r_e = 4
    var_2 = int(input("Ingrese el numero de su estrato socioeconmico: "))
    if var_2==1:
        e_s = 5
        valor_2=30
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))    
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==2:
        e_s = 5
        valor_2=24
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==3:
        e_s = 5
        valor_2=18
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==4:
        e_s = 5
        valor_2=6
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==5:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==6:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    else: 
        print("Se presento un error")
elif var_1=="gitano":
    valor_1=24
    r_e = 4
    var_2 = int(input("Ingrese el numero de su estrato socioeconmico: "))
    if var_2==1:
        e_s = 5
        valor_2=30
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))    
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==2:
        e_s = 5
        valor_2=24
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==3:
        e_s = 5
        valor_2=18
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==4:
        e_s = 5
        valor_2=6
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==5:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    elif var_2==6:
        e_s = 5
        valor_2=0
        var_3 = int(input("Introduzca los ingresos del nucleo familiar en pesos: "))
        if var_3<smmv:
            i_n_f = 6
            valor_3 = 45
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv)and(var_3<smmv*2):
            i_n_f = 6
            valor_3 = 27
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*2)and(var_3<smmv*4):
            i_n_f = 6
            valor_3 = 21
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif (var_3>=smmv*4)and(var_3<smmv*5):
            i_n_f = 6
            valor_3 = 12
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
        elif var_3>=smmv*5:
            i_n_f = 6
            valor_3 = 0
            puntaje = ((valor_1*r_e+valor_2*e_s+valor_3*i_n_f)/(r_e+e_s+i_n_f))
            if puntaje<20:
                print("El candidato no continua en el proceso de seleccion")
            elif puntaje>=20:
                print("El candidato continua en el proceso de seleccion")
    else: 
        print("Se presento un error")
        
else: 
    print("Se presento un error")