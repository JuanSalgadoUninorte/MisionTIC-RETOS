# AgregarComentario => StringField
# BotonEnviar => SubmitField
# BotonModificar => SubmitField
# BotonEliminar => SubmitField
# BotonVerMisComentarios => SubmitField

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class coment(FlaskForm):
    contenidoComent = StringField("Contenido", validators=[DataRequired(message="No dejar vacío")])
    IdComentario = StringField("IdComentario")
    IdUsuario = StringField("IdUsuario")

    botonEnviar = SubmitField("botonCrear", render_kw={"onmouseover" : "guardar()"})
    botonEliminar = SubmitField("botonEliminar", render_kw={"onmouseover" : "eliminar()"})
    botonModificar = SubmitField("botonActualizar", render_kw={"onmouseover" : "actualizar()"})
    botonVer = SubmitField("botonVisualizar", render_kw={"onmouseover" : "visualizar()"})