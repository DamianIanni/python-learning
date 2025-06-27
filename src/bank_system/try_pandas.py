import pandas as pd
import matplotlib.pyplot as plt

# Cargo el .csv
df = pd.read_csv("__data__/users.csv")

# Veo las primeras filas
print(df.head())

# Veo estadísticas generales
print(df.describe())

# Veo la info de columnas
print(df.info())

# Creo un gráfico de barras del balance de cada usuario
plt.bar(df["name"], df["balance"])
plt.title("Balance por usuario")
plt.xlabel("Nombre")
plt.ylabel("Balance")
plt.show()