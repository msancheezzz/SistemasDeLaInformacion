import json
import sqlite3
import pandas as pd
import matplotlib as mp

###### CONEXIONES Y FICHEROS #########
conexion = sqlite3.connect("bd1.db")
cursor = conexion.cursor()


#################EJERCICIO 4##################
ipsMasProblematicas = pd.read_sql_query("SELECT origen, COUNT(origen) AS cuenta FROM articulos GROUP BY origen ORDER BY cuenta DESC LIMIT 10;", conexion)
print(ipsMasProblematicas)

conexion.close()
