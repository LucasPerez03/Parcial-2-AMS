# Sistema de Gestión de Alumnos

Prototipo funcional desarrollado con Flask.

## Funcionalidades
- CRUD de alumnos
- Login con autenticación y contraseñas encriptadas con Bcrypt
- Predicción de promedio con regresión lineal (scikit-learn)

## Tecnologías
- Flask, SQLAlchemy, Flask-Login, Flask-Bcrypt
- scikit-learn, joblib
- Bootstrap 5
- PostgreSQL (producción) / SQLite (desarrollo)

## Correr localmente
```bash
pip install -r requirements.txt
python run.py
```