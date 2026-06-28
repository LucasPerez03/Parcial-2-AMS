from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import joblib

np.random.seed(42)
n = 200

nota_1 = np.random.uniform(1, 10, n)
nota_2 = np.random.uniform(1, 10, n)
asistencia = np.random.randint(0, 30, n)

promedio = (nota_1 + nota_2) / 2 + (asistencia / 30) * 0.5

x = np.column_stack((nota_1, nota_2, asistencia))
y = promedio

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
print("Modelo entrenado y guardado como 'model.pkl'")