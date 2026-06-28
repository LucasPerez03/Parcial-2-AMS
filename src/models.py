from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

login_manager = LoginManager()
bcrypt = Bcrypt()
bd = SQLAlchemy()

class Alumnos(bd.Model):
    id = bd.Column(bd.Integer,primary_key=True)
    nombre = bd.Column(bd.String(100), nullable=False)
    apellido = bd.Column(bd.String(100), nullable=False)
    edad = bd.Column(bd.Integer,nullable=False,default=18) 
    nota_1 = bd.Column(bd.Float,nullable=False,default=6 )
    nota_2 = bd.Column(bd.Float,nullable=False,default=6 ) 
    asistencia = bd.Column(bd.Integer,nullable=False,default=23) 

    @property 
    def promedio(self):
        return (self.nota_1 + self.nota_2) / 2
    
    @property 
    def aprobado(self):
        return self.promedio >= 6
    
    def __init__(self, nombre, apellido, edad, nota_1, nota_2, asistencia):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.asistencia = asistencia

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'nota_1':self.nota_1,
            'nota_2':self.nota_2,
            'asistencia':self.asistencia,
            "promedio": self.promedio,
            "aprobado": self.aprobado
            }
    
class Usuarios(bd.Model, UserMixin):
    id = bd.Column(bd.Integer, primary_key=True) 
    username = bd.Column(bd.String(80), unique=True, nullable=False)
    password_hash = bd.Column(bd.String(255), nullable=False)
    email = bd.Column(bd.String(120), unique=True, nullable=False)

    def __init__(self, username, password_hash,email):
        self.username = username
        self.password_hash = password_hash
        self.email = email