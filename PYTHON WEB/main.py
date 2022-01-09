from sqlite3.dbapi2 import Row
from flask import *
import sqlite3
import hashlib
from coment import coment
from markupsafe import escape
import os
from werkzeug.security import check_password_hash, generate_password_hash
variableGlobalVacia = None
sesion_iniciada = False
from flask import session
from procesar import *
IdUsuarioEnCuestion = ""
NombreUsuarioEnCuestion = ""
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
variableGlobalRol = ""

'''
REDIRECCIONAMIENTOS
'''

@app.route("/", methods=["GET"])
def index():
    global sesion_iniciada
    return render_template("paginaPrincipal.html")

@app.route("/registro/", methods=["GET", "POST"])
def registrarse():
    global sesion_iniciada
    return render_template("registro.html")

@app.route("/crudHabitacion/", methods=["GET", "POST"])
def crudHabitacion():
    global sesion_iniciada
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("crudHabitaciones.html", usuario2=usuario2, Nombre=Nombre)

@app.route("/formulario/", methods=["GET", "POST"])
def ira():
    global sesion_iniciada
    return render_template("iniciarSesion.html")

@app.route("/recuperarContrasena/", methods=["GET", "POST"])
def recuperarContra():
    global sesion_iniciada
    return render_template("recuperarContrasena.html")

@app.route("/msjenviadoRecuperar/", methods=["GET"])
def msjenviadoRecuperar():
    global sesion_iniciada
    return render_template("msjenviadoRecuperar.html")

@app.route("/rentarHabitacion/", methods=["GET"])
def rentar():
    global sesion_iniciada
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("Habitacion.html", usuario2=usuario2, Nombre=Nombre)

@app.route("/comentar/", methods=["GET", "POST"])
def comentar():
    global sesion_iniciada
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("Comentarios.html", usuario2=usuario2, Nombre=Nombre)

@app.route("/interfazUsuario/", methods=["GET", "POST"])
def interfazUsuario():
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    global sesion_iniciada
    return render_template("interfazUsuario.html", usuario2=usuario2, Nombre=Nombre)

@app.route("/interfazAdmin/", methods=["GET", "POST"])
def interfazAdmin():
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    global sesion_iniciada
    return render_template("Inicio-Administrador.html", usuario2=usuario2, Nombre=Nombre)

@app.route("/interfazSuperAdmin/", methods=["GET", "POST"])
def interfazSuperAdmin():
    global sesion_iniciada
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("Inicio-Super-Administrador.html", usuario2=usuario2, Nombre=Nombre)

'''
REDIRECCIONAMIENTOS
'''
'''
metodos importantes
'''
@app.route("/iniciarSesion/", methods=["GET", "POST"])
def iniciarSesion():
    usuario2 = escape(request.form["usuario"])
    global variableGlobalRol
    global sesion_iniciada
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    contrasena2 = escape(request.form["contrasena"])
    with sqlite3.connect("JumeirahEmiratesDB.db") as conn:
        cur = conn.cursor()
        variableVector = cur.execute(f"SELECT Contrasena FROM USUARIOS WHERE IdUsuario = '{usuario2}'").fetchone()
        if variableVector != None:
            variableInterna = variableVector[0]
            session.clear()
            if check_password_hash(variableInterna, contrasena2):
                session["usuario"] = usuario2
                rolUsu = cur.execute(f"SELECT IdRol FROM USUARIOS WHERE IdUsuario = '{usuario2}'").fetchone()
                Nombre2 = cur.execute(f"SELECT NOMBRES FROM USUARIOS WHERE IdUsuario = '{usuario2}'").fetchone()
                Nombre = Nombre2[0]
                variableGlobalRol = Nombre
                sesion_iniciada = True
                IdUsuarioEnCuestion = usuario2
                NombreUsuarioEnCuestion = Nombre
                if rolUsu[0] == 1:
                    return render_template("Inicio-Administrador.html", usuario2=usuario2, Nombre=Nombre)#form = form significa todos los datos que van a pasar
                if rolUsu[0] == 3:
                    return render_template("interfazUsuario.html", usuario2=usuario2, Nombre=Nombre)#form = form significa todos los datos que van a pasar
                elif rolUsu[0] == 2:
                    return render_template("Inicio-Super-Administrador.html", usuario2=usuario2,  Nombre=Nombre)#form = form significa todos los datos que van a pasar
        else: 
            return ("<script>alert('Usuario inexistente o clave false \nIntente nuevamente...');window.location.href='/formulario/';</script>")
    return "<script>alert('Usuario inexistente o clave false \nIntente nuevamente...');window.location.href='/formulario/';</script>"

@app.route('/cerrarSesion/', methods=["POST", "GET"])
def cerrarSesion():
    if "usuario" in session:#aquí amarro para que él esté logueado para que pueda entrar a los contenidos, sino, no entra
        session.pop("usuario", None)
        return render_template("paginaPrincipal.html")
    else:
        return "<script>alert('La sesión ya ha sido cerrada o nunca fue abierta....');window.location.href='/';</script>"

@app.before_request
def conBeforeRequest():
    global variableGlobalRol
    global sesion_iniciada
    if "usuario" not in session and request.endpoint in ['crudHabitacion', 'rentar', 'comentar', 'interfazUsuario', 'interfazAdmin', 'interfazSuperAdmin', 
    'ActualizarInfo', 'irAreserva', 'crudReservas', 'reservar', 'actReserva', 'listarReservas', 'eliminarReserva', 'crearReservaAdmin', 'comenta_dos',
    'enviar', 'gestionComentarios', 'listarCalificaciones', 'eliminarCalificacion', 'calificanos', 'creandoHabitacion', 'eliminarHabitacion', 
    'listarHabitaciones', 'listarHabi', 'listarUsu', 'crearUsu', 'crudPers', 'editUsuAd', 'eliminarUsuario', 'listarCalificacionesPropias', 'listarReservasPropias', 'crudCaliPropias', 'crudReservasPropias']:
        return redirect(url_for("index"))
    if "usuario" in session and variableGlobalRol == "1" :
        sesion_iniciada = True
        return redirect(url_for("interfazAdmin"))
    elif "usuario" in session and variableGlobalRol == "2" :
        sesion_iniciada = True
        return redirect(url_for("interfazSuperAdmin"))
    elif ("usuario" in session) and (variableGlobalRol == "3") and request.endpoint in ['creandoHabitacion', 'eliminarHabitacion', 
    'listarHabitaciones', 'listarHabi', 'listarUsu', 'crearUsu', 'crudPers', 'editUsuAd', 'eliminarUsuario', 'crearReservaAdmin', 'crudReservas', 'interfazAdmin', 'interfazSuperAdmin', 'crudHabitacion']:
        sesion_iniciada = True
        return redirect(url_for("interfazUsuario"))
'''
fin metodos
'''
'''
Comienzo de CRUDS
'''
#ACTUALIZAR INFO POR USUARIO
@app.route("/formularioUpdate/", methods=["GET", "POST"])
def iraUpdate():
    global sesion_iniciada
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("ActualizarInformacionUsuario.html", usuario2=usuario2, Nombre=Nombre)

@app.route('/interfazUsuario/ActualizarInfo/', methods=['GET', 'POST'])
def ActualizarInformacionUsuario():
    global sesion_iniciada
    if request.method == "POST":
        sesion_iniciada = True
        user = escape(request.form['id'])
        names = escape(request.form['nombres'])
        last_n = escape(request.form['apellidos'])
        tel = escape(request.form['telefono'])
        addrs = escape(request.form['direccion'])
        mail = escape(request.form['email'])
        birth = escape(request.form['nacimiento'])

        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            cur.execute("UPDATE USUARIOS SET Nombres = ?, Apellidos = ?, Telefono = ?, Direccion = ?, CorreoElectronico = ?, FechaNacimiento = ? WHERE IdUsuario = ?", [names, last_n, tel, addrs, mail, birth, user])
            conn.commit()#Confirmación de inserción de datos :)
            return "<script>alert('Datos Actualizados Exitosamente!');window.location.href='/interfazUsuario/';</script>"
    return "Error, comuníquese con nosotros para darle solución a este problema. <a href='/'>Volver al inicio</a>"

@app.route('/interfazUsuario/ActualizarInfo/', methods=['GET', 'POST'])
def ActualizarInfo():
    global sesion_iniciada
    sesion_iniciada = True
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template('ActualizarInformacionUsuario.html', usuario2=usuario2, Nombre=Nombre)

#//RESERVAS
@app.route("/irAreserva/", methods=["GET", "POST"])
def irAreserva():
    global sesion_iniciada
    sesion_iniciada = True
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    habitacion = escape(request.form['habitacion'])
    return render_template("generarReserva.html", habitacion=habitacion, Nombre=Nombre, usuario2=usuario2)

@app.route("/crudReservas/", methods=["GET", "POST"])
def crudReservas():
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("crudReservas.html", usuario2=usuario2, Nombre=Nombre)

@app.route('/reservar/', methods=["POST"])
def reservar():
    if request.method == "POST":
        IdUsuario = escape(request.form["IdUsuario"])
        IdHabitacion = escape(request.form["IdHabitacion"])
        Fecha = escape(request.form["fechaFinal"])
        FechaInicial = escape(request.form["fechaInicial"])
        Disponibilidad = "No Disponible"
        Estado = "Activa"
        with sqlite3.connect("JumeirahEmiratesDB.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO RESERVAS (IdUsuario, IdHabitacion, DiaEntrada, DiaSalida, EstadoReserva) values (?, ?, ?, ?, ?)", (IdUsuario, IdHabitacion, FechaInicial, Fecha, Estado))
            con.commit()
            if con.commit:
                cur.execute("UPDATE HABITACIONES SET Disponibilidad = ? WHERE IdHabitacion = ?", [Disponibilidad, IdHabitacion])
                con.commit()
            return "<script>alert('Reserva Guardada Exitosamente');window.location.href='/crudReservas/';</script>"
    return "No se pudo guardar"

@app.route('/actReserva/', methods=["POST"])
def actReserva():
    if request.method == "POST":
        IdReserva = escape(request.form['IdReserva'])
        IdUsuario = escape(request.form["IdUsuario"])
        IdHabitacion = escape(request.form["IdHabitacion"])
        Fecha = escape(request.form["diaSalida"])
        FechaInicial = escape(request.form["diaEntrada"])
        Estado = "Activa"
        with sqlite3.connect("JumeirahEmiratesDB.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE RESERVAS SET IdUsuario = ?, IdHabitacion = ?, DiaEntrada = ?, DiaSalida = ?, EstadoReserva = ? WHERE IdReserva = ?", [IdUsuario, IdHabitacion, Fecha, FechaInicial, Estado, IdReserva])
            con.commit()
            return "<script>alert('Reserva Editada Exitosamente');window.location.href='/crudReservas/';</script>"
    return "No se pudo guardar"

@app.route("/listarReservas/",  methods=["GET", "POST"])
def listarReservas():
    if request.method == "POST" or request.method == "GET":
        SQL = "SELECT * FROM RESERVAS"
        fISeleccion = seleccion(SQL)
        global IdUsuarioEnCuestion
        global NombreUsuarioEnCuestion
        usuario2 = IdUsuarioEnCuestion
        Nombre = NombreUsuarioEnCuestion
        return render_template("listarReservas.html", fISeleccion=fISeleccion, usuario2=usuario2, Nombre=Nombre)
    return render_template("listarReservas.html")

@app.route("/eliminarReserva/", methods=["GET", "POST"])
def eliminarReserva():
    if request.method=="POST":
        IdReserva = escape(request.form['IdReserva'])
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            cur.execute("DELETE FROM RESERVAS WHERE IdReserva = ?", [IdReserva])
            if conn.total_changes > 0:
                return "<script>alert('La reserva ha sido eliminada!');window.location.href='/crudReservas/';</script>"
    return "Error, comuníquese con nosotros para darle solución a este problema. <a href='paginaPrincipal.html'>Volver al inicio</a>"

@app.route("/crearReserva/", methods=["GET", "POST"])
def crearReservaAdmin():
    if request.method == "POST":
        IdUsuario = escape(request.form["IdUsuario"])
        IdHabitacion = escape(request.form["IdHabitacion"])
        Fecha = escape(request.form["diaSalida"])
        FechaInicial = escape(request.form["diaEntrada"])
        Disponibilidad = "No Disponible"
        Estado = "Activa"
        with sqlite3.connect("JumeirahEmiratesDB.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO RESERVAS (IdUsuario, IdHabitacion, DiaEntrada, DiaSalida, EstadoReserva) values (?, ?, ?, ?, ?)", (IdUsuario, IdHabitacion, FechaInicial, Fecha, Estado))
            con.commit()
            if con.commit:
                cur.execute("UPDATE HABITACIONES SET Disponibilidad = ? WHERE IdHabitacion = ?", [Disponibilidad, IdHabitacion])
                con.commit()
            return "<script>alert('Reserva Guardada Exitosamente');window.location.href='/';</script>"
    return "No se pudo guardar"

#//RESERVAS

#//COMENTARIOS


#//COMENTARIOS

@app.route('/CrearComentario/', methods=["POST"])
def enviar():
    form = coment()
    if request.method == "POST":
        IdUsuario = escape(request.form["IdUsuario"])
        IdHabitacion = escape(request.form["IdHabitacion"])
        Fecha = escape(request.form["fechaFinal"])
        Comentario = escape(request.form["Comentario"])
        Calificacion = escape(request.form["Calificacion"])
        with sqlite3.connect("JumeirahEmiratesDB.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO CALIFICACIONES (FechaCalificacion, Calificacion, IdHabitacion, IdUsuario, Comentario) values (?, ?, ?, ?, ?)", (Fecha,Calificacion,IdHabitacion,IdUsuario,Comentario))
            con.commit()
            return "<script>alert('Calificación Guardada Exitosamente');window.location.href='/gestionComentarios/';</script>"
    return "No se pudo guardar"

@app.route("/gestionComentarios/",  methods=["GET", "POST"])
def gestionComentarios():
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("GestionComentarios.html", usuario2=usuario2, Nombre=Nombre)

@app.route("/listarCalificaciones/",  methods=["GET", "POST"])
def listarCalificaciones():
    if request.method == "POST" or request.method == "GET":
        SQL = "SELECT * FROM CALIFICACIONES"
        global IdUsuarioEnCuestion
        global NombreUsuarioEnCuestion
        usuario2 = IdUsuarioEnCuestion
        Nombre = NombreUsuarioEnCuestion
        fISeleccion = seleccion(SQL)
        return render_template("listarCalificaciones.html", fISeleccion=fISeleccion, usuario2=usuario2, Nombre=Nombre)
    return render_template("listarCalificaciones.html")

@app.route("/eliminarComentario/", methods=["GET", "POST"])
def eliminarCalificacion():
    if request.method=="POST":
        IdCalificacion = escape(request.form['Calificacion'])
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            cur.execute("DELETE FROM CALIFICACIONES WHERE IdCalificacion = ?", [IdCalificacion])
            if conn.total_changes > 0:
                return "<script>alert('La calificación ha sido eliminada!');window.location.href='/gestionComentarios/';</script>"
    return "Error, comuníquese con nosotros para darle solución a este problema. <a href='paginaPrincipal.html'>Volver al inicio</a>"

@app.route("/calificanos/", methods=["GET", "POST"])
def calificanos():
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("calificaciones.html",usuario2=usuario2, Nombre=Nombre)

#//Comentarios
#/HABITACIONES
@app.route("/crearHabitacion/", methods=["POST", "GET"])
def creandoHabitacion():
    if request.method=="POST":
        disponibilidad = escape(request.form['disponibilidad'])
        IdCreador = escape(request.form['IdCreador'])
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            cur.execute("INSERT INTO HABITACIONES (Disponibilidad, IdCreador) VALUES (?,?)", (disponibilidad,IdCreador))
            conn.commit()#Confirmación de inserción de datos :)
            return "<script>alert('La calificación ha sido eliminada!');window.location.href='/GestionComentarios/';</script>"
    return "Error, comuníquese con nosotros para darle solución a este problema. <a href='paginaPrincipal.html'>Volver al inicio</a>"

@app.route("/eliminarHabitacion/", methods=["GET", "POST"])
def eliminarHabitacion():
    if request.method=="POST":
        IdHabitacion = escape(request.form['IdHabitacion'])
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            cur.execute("DELETE FROM HABITACIONES WHERE IdHabitacion = ?", [IdHabitacion])
            if conn.total_changes > 0:
                return "<script>alert('La habitación ha sido eliminada!');window.location.href='/crudHabitacion/';</script>"
    return "Error, comuníquese con nosotros para darle solución a este problema. <a href='paginaPrincipal.html'>Volver al inicio</a>"

@app.route('/editarHabitacion/', methods=["POST"])
def actualizarHabitacion():
    if request.method == "POST":
        IdHabitacion = escape(request.form['IdHabitacion'])
        dis = escape(request.form['disponibilidad'])
        IdCreador = escape(request.form['IdCreador'])
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            cur.execute("UPDATE HABITACIONES SET Disponibilidad = ?, IdCreador = ? WHERE IdHabitacion = ?", [dis, IdCreador, IdHabitacion])
            conn.commit()#Confirmación de inserción de datos :)
            return "<script>alert('La habitación ha sido editada');window.location.href='/crudHabitacion/';</script>"
    return "No se pudo actualizar T_T"

@app.route("/listarHabitaciones/",  methods=["GET", "POST"])
def listarHabitaciones():
    if request.method == "POST" or request.method == "GET":
        SQL = "SELECT * FROM HABITACIONES"
        fISeleccion = seleccion(SQL)
        global IdUsuarioEnCuestion
        global NombreUsuarioEnCuestion
        usuario2 = IdUsuarioEnCuestion
        Nombre = NombreUsuarioEnCuestion
        return render_template("listarHabitaciones.html", fISeleccion=fISeleccion, usuario2=usuario2, Nombre=Nombre)
    return render_template("listarHabitaciones.html")

@app.route("/busqueda/",  methods=["GET", "POST"])
def buqueda():
    if request.method == "POST" or request.method == "GET":
        z = "Disponible"
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            variableVector = "SELECT IdHabitacion FROM HABITACIONES WHERE Disponibilidad = 'Disponible'"
            fISeleccion = seleccion(variableVector)
            global IdUsuarioEnCuestion
            global NombreUsuarioEnCuestion
            usuario2 = IdUsuarioEnCuestion
            Nombre = NombreUsuarioEnCuestion
            return render_template("busqueda.html", fISeleccion=fISeleccion, usuario2=usuario2, Nombre=Nombre)
    return render_template("busqueda.html")

@app.route("/listarHabitaciones/",  methods=["GET", "POST"])
def listarHabi():
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("listarHabitaciones.html", usuario2=usuario2, Nombre=Nombre)
#/HABITACIONES

#/PERSONAS
@app.route("/crearUsuario/", methods=["GET", "POST"])
def crearUsu():
    if request.method == "POST":
        user = escape(request.form['id'])
        names = escape(request.form['name'])
        last_n = escape(request.form['last'])
        tel = escape(request.form['tel'])
        addrs = escape(request.form['add'])
        mail = escape(request.form['mail'])
        birth = escape(request.form['birth'])
        passw = escape(request.form['passw'])
        rol = 3
        variablez = generate_password_hash(passw)
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            cur.execute("INSERT INTO USUARIOS (IdUsuario, Nombres, Apellidos, FechaNacimiento, CorreoElectronico, Direccion, Telefono, Contrasena, IdRol) VALUES (?,?,?,?,?,?,?,?,?)", (user, names, last_n, birth, mail, addrs, tel, variablez, rol))
            conn.commit()#Confirmación de inserción de datos :)
            return "<script>alert('El usuario ha sido creado exitosamente!');window.location.href='/';</script>"
    return "Error, comuníquese con nosotros para darle solución a este problema. <a href='paginaPrincipal.html'>Volver al inicio</a>"

@app.route("/crudPersonas/",  methods=["GET", "POST"])
def crudPers():
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("crudUsuarios.html", usuario2=usuario2, Nombre=Nombre)

@app.route("/listarUsuarios/",  methods=["GET", "POST"])
def listarUsu():
    if request.method == "POST" or request.method == "GET":
        SQL = "SELECT * FROM USUARIOS"
        fISeleccion = seleccion(SQL)
        global IdUsuarioEnCuestion
        global NombreUsuarioEnCuestion
        usuario2 = IdUsuarioEnCuestion
        Nombre = NombreUsuarioEnCuestion
        return render_template("listarUsuarios.html", fISeleccion=fISeleccion, usuario2=usuario2, Nombre=Nombre)
    return render_template("listarUsuarios.html")

@app.route("/editarUsuarioAdmin/", methods=["GET", "POST"])
def editUsuAd():
    if request.method == "POST":
        user = escape(request.form['id'])
        names = escape(request.form['name'])
        last_n = escape(request.form['last'])
        tel = escape(request.form['tel'])
        addrs = escape(request.form['add'])
        mail = escape(request.form['mail'])
        birth = escape(request.form['birth'])
        passw = escape(request.form['passw'])
        rol = escape(request.form['rol'])
        variablez = generate_password_hash(passw)
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            cur.execute("UPDATE USUARIOS SET Nombres = ?, Apellidos = ?, FechaNacimiento = ?, CorreoElectronico = ?, Direccion = ?, Telefono = ?, Contrasena = ?, IdRol = ? WHERE IdUsuario = ?", [names, last_n, birth, mail, addrs, tel, variablez, rol, user])
            conn.commit()#Confirmación de inserción de datos :)
            return "<script>alert('El usuario ha sido editado exitosamente!');window.location.href='/crudPersonas/';</script>"
    return "Error, comuníquese con nosotros para darle solución a este problema. <a href='paginaPrincipal.html'>Volver al inicio</a>"

@app.route("/crearUsuarioAdmin/", methods=["GET", "POST"])
def crearUsuAd():
    if request.method == "POST":
        user = escape(request.form['id'])
        names = escape(request.form['name'])
        last_n = escape(request.form['last'])
        tel = escape(request.form['tel'])
        addrs = escape(request.form['add'])
        mail = escape(request.form['mail'])
        birth = escape(request.form['birth'])
        passw = escape(request.form['passw'])
        rol = escape(request.form['rol'])
        variablez = generate_password_hash(passw)
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            cur.execute("INSERT INTO USUARIOS (IdUsuario, Nombres, Apellidos, FechaNacimiento, CorreoElectronico, Direccion, Telefono, Contrasena, IdRol) VALUES (?,?,?,?,?,?,?,?,?)", (user, names, last_n, birth, mail, addrs, tel, variablez, rol))
            conn.commit()#Confirmación de inserción de datos :)
            return "<script>alert('El usuario ha sido creado exitosamente!');window.location.href='/crudPersonas/';</script>"
    return "Error, comuníquese con nosotros para darle solución a este problema. <a href='paginaPrincipal.html'>Volver al inicio</a>"

@app.route("/eliminarUsuario/", methods=["GET", "POST"])
def eliminarUsuario():
    if request.method=="POST":
        IdUsuario = escape(request.form['IdUsuario'])
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            cur.execute("DELETE FROM USUARIOS WHERE IdUsuario = ?", [IdUsuario])
            if conn.total_changes > 0:
                return "<script>alert('El usuario ha sido eliminado!');window.location.href='/crudPersonas/';</script>"
    return "Error, comuníquese con nosotros para darle solución a este problema. <a href='paginaPrincipal.html'>Volver al inicio</a>"
#/PERSONAS 
'''
Final de CRUDS
'''
#Rol de usuarios
# 
@app.route("/calificacionesPropias/",  methods=["GET", "POST"])
def listarCalificacionesPropias():
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    if request.method == "POST" or request.method == "GET":
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            conn.row_factory = sqlite3.Row#Gestiona la db
            cur = conn.cursor()#manipula la db
            cur.execute("SELECT * FROM CALIFICACIONES WHERE IdUsuario = ?", [usuario2])
            fISeleccion = cur.fetchall()#La consulta es asignada y procesada
            if fISeleccion is None:
                return "<script>alert('No hay calificaciones suyas!');window.location.href='listarCalificacionesUsuario.html';</script>"
            else:
                return render_template("listarCalificacionesUsuario.html", fISeleccion=fISeleccion, usuario2=usuario2, Nombre=Nombre)

@app.route("/reservasPropias/",  methods=["GET", "POST"])
def listarReservasPropias():
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    if request.method == "POST" or request.method == "GET":
        with sqlite3.connect("JumeirahEmiratesDB.db") as conn:#Manejador de contexto ->conexion
            conn.row_factory = sqlite3.Row#Gestiona la db
            cur = conn.cursor()#manipula la db
            cur.execute("SELECT * FROM RESERVAS WHERE IdUsuario = ?", [usuario2])
            fISeleccion = cur.fetchall()#La consulta es asignada y procesada
            if fISeleccion is None:
                return "<script>alert('No hay calificaciones suyas!');window.location.href='listarReservasUsuario.html';</script>"
            else:
                return render_template("listarReservasUsuario.html", fISeleccion=fISeleccion, usuario2=usuario2, Nombre=Nombre)

@app.route("/crudCalificacionesPropias/", methods=["GET", "POST"])
def crudCaliPropias():
    global sesion_iniciada
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("crudUsuariocalificaciones.html", usuario2=usuario2, Nombre=Nombre)

@app.route("/crudReservasUsuario/", methods=["GET", "POST"])
def crudReservasPropias():
    global sesion_iniciada
    global IdUsuarioEnCuestion
    global NombreUsuarioEnCuestion
    usuario2 = IdUsuarioEnCuestion
    Nombre = NombreUsuarioEnCuestion
    return render_template("crudReservasUsuario.html", usuario2=usuario2, Nombre=Nombre)
# #

if __name__ == '__main__':
    app.run(debug=True)