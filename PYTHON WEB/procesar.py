import sqlite3
variableNombreBD = "JumeirahEmiratesDB.db"

def seleccion(variableSQL):
    with sqlite3.connect(variableNombreBD) as conn:
        cur = conn.cursor()
        variableResultado = cur.execute(variableSQL).fetchall()
        return variableResultado

def accion(variableSQL):
    with sqlite3.connect(variableNombreBD) as conn:
        cur = conn.cursor()
        variableResultado = cur.execute(variableSQL).rowcount()
        if variableResultado != 0:
            conn.commit()
        return variableResultado