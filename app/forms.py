from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired

class SegitigaForm(FlaskForm):
    number = IntegerField('Input Angka', validators=[DataRequired()])
    tipe = RadioField('Type', choices=[('segitiga', 'Segitiga'), ('ganjil', 'Ganjil'), ('prima', 'Prima')])
    submit = SubmitField('Submit')