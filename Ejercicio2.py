import pandas as pd
import json
import sqlite3

data = pd.read_csv("Data/alerts.csv")
dev = open("data/devices.json")
devices = json.load(dev)
rows = data.shape[0]
conexion = sqlite3.connect("bd1.db")
cursor = conexion.cursor()


############## SELECCIONES #####################

analisis_analisis = pd.read_sql_query("SELECT * FROM analisis", conexion)

data.to_sql("articulos", conexion, if_exists="replace", index=False)
cursor.execute("SELECT COUNT(*) FROM dispositivos")
n_dispositivos = cursor.fetchone()
print("Número de dispositivos: " + str(n_dispositivos[0]))
cursor.execute("SELECT COUNT(*) FROM articulos")
n_alertas = cursor.fetchone()
print("Número de alertas: " + str(n_alertas[0]))

cursor.execute("SELECT AVG(n_puertos_abiertos) FROM analisis")
media_abiertos= cursor.fetchone()
print("Media de puertos abiertos: " + "{:.2f}".format(media_abiertos[0]) + "\nDesviación estándar de los puertos abiertos: " + "{:.2f}".format(analisis_analisis['n_puertos_abiertos'].std()))

cursor.execute("SELECT AVG(servicios_inseguros) FROM analisis")
media_inseguros= cursor.fetchone()
print("Media de servicios inseguros: " + "{:.2f}".format(media_inseguros[0]) + "\nDesviación estándar de servicios inseguros: " + "{:.2f}".format(analisis_analisis['servicios_inseguros'].std()))

cursor.execute("SELECT AVG(vulnerabilidades_detectadas) FROM analisis")
media_vulnerabilidades= cursor.fetchone()
##cursor.execute("SELECT STDEV(vulnerabilidades_detectadas) FROM analisis")
print("Media de vulnerabilidades detectadas: " + "{:.2f}".format(media_vulnerabilidades[0]) + "\nDesviación estándar de vulnerabilidades detectadas: " + "{:.2f}".format(analisis_analisis['vulnerabilidades_detectadas'].std()))

cursor.execute("SELECT max(n_puertos_abiertos) FROM analisis")
max_abiertos= cursor.fetchone()
cursor.execute("SELECT min(n_puertos_abiertos) FROM analisis")
min_abiertos= cursor.fetchone()
print("Maximo de puertos abiertos: " + str(max_abiertos[0]) + "\nMínimo de puertos abiertos: " + str(min_abiertos[0]))

cursor.execute("SELECT max(vulnerabilidades_detectadas) FROM analisis")
max_vuln= cursor.fetchone()
cursor.execute("SELECT min(vulnerabilidades_detectadas) FROM analisis")
min_vuln= cursor.fetchone()
print("Máximo de vulnerabilidades: " + str(max_vuln[0]) + "\nMínimo de vulnerabilidades: " + str(min_vuln[0]))

