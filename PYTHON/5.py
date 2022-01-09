import csv
def ejercicio():
    with open("data.csv", mode="r", encoding="utf-8-sig") as archivo:
        lector = csv.reader(archivo)
        ciudad = input()
        etniaContador = [
            ["sin reconocimiento", 0],
            ["afrodescendiente", 0],
            ["indigena", 0],
            ["raizal", 0],
            ["palenquero", 0],
            ["gitano", 0]
        ]
        listaDineros,postulados = [],[]
        contadorAprobados =  0
        for pos, linea in enumerate(lector):
            if pos>0:
                # postulados.append([str(linea[2]), str(linea[4]), int(linea[6]), int(linea[7])])
                if linea[2] == ciudad and linea[7]=="1":
                    postulado=linea[4]
                    sal=int(linea[6])
                    listaDineros.append(sal)
                    if postulado == "sin reconocimiento":
                        etniaContador[0][1] += 1
                    elif postulado == "afrodescendiente":
                        etniaContador[1][1] += 1
                    elif postulado == "indigena":
                        etniaContador[2][1] += 1
                    elif postulado == "raizal":
                        etniaContador[3][1] += 1
                    elif postulado == "palenquero":
                        etniaContador[4][1] += 1
                    elif postulado == "gitano":
                        etniaContador[5][1] += 1
                    postulados.append(postulado)
                    contadorAprobados += 1
                    #etnia_Contador.sort(key=lambda x: x[1])
                    #etnia_Contador.sort(key=lambda x: x[0], reverse=True)
    etnia_Contador = etniaContador.copy()
    etnia_Contador = sorted(etnia_Contador, key=lambda x: (x[1], x[0]), reverse=True)
    print(contadorAprobados)
    minimo = min(listaDineros)
    maximo = max(listaDineros)
    promedio = sum(listaDineros)/len(listaDineros)
    print(f"{minimo} {maximo} {promedio:.2f}")
    for i in range(6):
        print(etnia_Contador[i][0], "", etnia_Contador[i][1])
ejercicio()