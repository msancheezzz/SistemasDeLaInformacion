import json
import sqlite3
import pandas as pd
import matplotlib as mp

###### CONEXIONES Y FICHEROS #########
conexion = sqlite3.connect("bd1.db")
cursor = conexion.cursor()


#################EJERCICIO 4##################
ipsMasProblematicas = pd.read_sql_query("SELECT origen, COUNT(origen) AS cuenta FROM articulos GROUP BY origen ORDER BY cuenta DESC LIMIT 10;", conexion)
graph1 = mp.bar(ipsMasProblematicas['origen'], ipsMasProblematicas['cuenta'], width=0.8, bottom=0)
mp.xlabel("Número de apariciones")
mp.ylabel("Direcciones IP")
mp.title("10 IPs origen más comunes")
mp.show()

nAlertasPorTiempo = pd.read_sql_query("SELECT strftime('%m %d', timestamp) dias, COUNT(*) cuenta FROM articulos GROUP BY dias;", conexion)
dias = list(range(1, 66))
mp.plot(dias, nAlertasPorTiempo['cuenta'])
mp.xlabel("Días desde el inicio de la captura")
mp.ylabel("Número de apariciones")
mp.title("Alertas por tiempo (día)")
mp.show()

nAlertasPorCategoria = pd.read_sql_query("SELECT clasificacion, COUNT(*) cuenta FROM articulos GROUP BY clasificacion;", conexion)
mp.barh(nAlertasPorCategoria['clasificacion'], nAlertasPorCategoria['cuenta'])
mp.xlabel("Categorías")
mp.ylabel("Número de apariciones")
mp.title("Alertas por categoría")
mp.show()

masVulns = pd.read_sql_query("SELECT dispositivos.id nombre, analisis.servicios_inseguros + analisis.vulnerabilidades_detectadas suma FROM dispositivos JOIN analisis ON dispositivos.analisis=analisis.id ORDER BY suma DESC;", conexion)
mp.barh(masVulns['nombre'], masVulns['suma'])
mp.xlabel("Nombre del dispositivo")
mp.ylabel("Suma de vulnerabilidad")
mp.title("Dispositivos más vulnerables")
mp.show()

mediaPuertosAbiertos = pd.read_sql_query("SELECT servicios, AVG(n_puertos_abiertos) media FROM analisis GROUP BY servicios;", conexion)
mp.bar(mediaPuertosAbiertos['servicios'], mediaPuertosAbiertos['media'])
mp.xlabel("Número de servicios detectados")
mp.ylabel("Media de puertos abiertos")
mp.title("Media de puertos frente a servicios detectados")
mp.show()

mediaPuertosAbiertos = pd.read_sql_query("SELECT servicios_inseguros, AVG(n_puertos_abiertos) media FROM analisis GROUP BY servicios;", conexion)
mp.bar(mediaPuertosAbiertos['servicios_inseguros'], mediaPuertosAbiertos['media'])
mp.xlabel("Número de servicios inseguros")
mp.ylabel("Media de puertos abiertos")
mp.title("Media de puertos frente a servicios inseguros")
mp.show()

conexion.close()
