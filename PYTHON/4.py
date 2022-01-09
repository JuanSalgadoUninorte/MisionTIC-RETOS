DiccionarioEtnia = {
    1: "sin reconocimiento",
    2: "afrodescendiente",
    3: "indigena",
    4: "raizal",
    5: "palenquero",
    6: "gitano"
}
Diccionario_valor_etnia = {
    "sin reconocimiento": 0,
    "afrodescendiente": 12,
    "indigena": 15,
    "raizal": 18,
    "palenquero": 21,
    "gitano": 24
}
Diccionario_valor_estrato = {
    1: 30,
    2: 24,
    3: 18,
    4: 6,
    5: 0,
    6: 0
}
lista_auxiliar_etnia_temporal = []
lista_etnias_general =[]
matriz=[]
etnia = []
estrato = []
entrada_a_1 = []
ingreso_familiar = []
repeticiones = int(input())
for i in range(1, repeticiones+1):
    etnia_entrada = input().split(" ")
    entrada_a = [int(x) for x in etnia_entrada]
    etnia.append(entrada_a)
for i in range(1, repeticiones+1):
    estrato_entrada = input().split(" ")
    entrada_b = [int(x) for x in estrato_entrada]
    estrato.append(entrada_b)
for i in range(1, repeticiones+1):
    ingreso_entrada = input().split(" ")
    entrada_c = [int(x) for x in ingreso_entrada]
    ingreso_familiar.append(entrada_c)
l = 0
cuentasDias = []
def crearCuenta():
    return {
        "etnias": {
            "sin reconocimiento": 0,
            "afrodescendiente": 0,
            "indigena": 0,
            "raizal": 0,
            "palenquero": 0,
            "gitano": 0
        },
        "aceptados": 0
    }
for i in range(7):#dia
    cuentasDias.append(crearCuenta())
    for j in range(repeticiones):#estudiante
        cuentasDias[i]["etnias"][DiccionarioEtnia[etnia[j][i]]] += 1
        etniaActual = etnia[j][i]
        if etniaActual == 1:
            x1 = 0
        elif etniaActual == 2:
            x1 = 12
        elif etniaActual == 3:
            x1 = 15
        elif etniaActual == 4:
            x1 = 18
        elif etniaActual == 5:
            x1 = 21
        elif etniaActual == 6:
            x1 = 24
        estratoActual = estrato[j][i]
        if estratoActual == 1:
            x2 = 30
        elif estratoActual == 2:
            x2 = 24
        elif estratoActual == 3:
            x2 = 18
        elif estratoActual == 4:
            x2 = 6
        else:
            x2 = 0
        SMMLV = ingreso_familiar[j][i]/908526
        if SMMLV < 1:
            x3 = 45
        elif 1 <= SMMLV < 2:
            x3 = 27
        elif 2 <= SMMLV < 4:
            x3 = 21
        elif 4 <= SMMLV < 5:
            x3 = 12
        else:
            x3 = 0
        resultadoEstudiante = (x1*4+x2*5+x3*6)/15
        if resultadoEstudiante >= 20:
            cuentasDias[i]["aceptados"]+=1
totalEtniasSemana = {
    "sin reconocimiento": 0,
    "afrodescendiente": 0,
    "indigena": 0,
    "raizal": 0,
    "palenquero": 0,
    "gitano": 0
}
salidaEtnias = ""
for i  in range(7):
    etniaMenor = 0
    stringEtnia = ""
    for k in cuentasDias[i]["etnias"]:
        totalEtniasSemana[k] += cuentasDias[i]["etnias"][k]
        if (cuentasDias[i]["etnias"][k] < etniaMenor and cuentasDias[i]["etnias"][k] != 0) or etniaMenor == 0:
            etniaMenor = cuentasDias[i]["etnias"][k]
            stringEtnia = k
    
    if i != 0:
        salidaEtnias += ","
    salidaEtnias+=stringEtnia
print(salidaEtnias)
    
etniaMenor = 0
stringEtnia = ""
for k  in totalEtniasSemana:
    if (totalEtniasSemana[k] < etniaMenor and totalEtniasSemana[k] != 0) or etniaMenor == 0:
        etniaMenor = totalEtniasSemana[k]
        stringEtnia = k
print(stringEtnia)
salidaEtnias = ""
for i  in range(7):
    etniaMayor = cuentasDias[i]["etnias"]["sin reconocimiento"]
    stringEtnia = "sin reconocimiento"
    for k in cuentasDias[i]["etnias"]:
        if cuentasDias[i]["etnias"][k] > etniaMayor:
            etniaMayor = cuentasDias[i]["etnias"][k]
            stringEtnia = k
    
    if i != 0:
        salidaEtnias += ","
    salidaEtnias+=stringEtnia
print(salidaEtnias)
    
etniaMayor = totalEtniasSemana["sin reconocimiento"]
stringEtnia = "sin reconocimiento"
for k  in totalEtniasSemana:
    if totalEtniasSemana[k] > etniaMayor:
        etniaMayor = totalEtniasSemana[k]
        stringEtnia = k
print(stringEtnia)
for i in range(7):
    if i != 0:
        print(" ", end="")
    print(cuentasDias[i]["aceptados"], end="")