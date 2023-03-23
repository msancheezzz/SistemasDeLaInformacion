import json
import sqlite3
import pandas as pd
###### CONEXIONES Y FICHEROS #########
data = pd.read_csv("Data/alerts.csv")
dev = open("data/devices.json")
devices = json.load(dev)
rows = data.shape[0]
conexion = sqlite3.connect("bd1.db")
cursor = conexion.cursor()

######## CREACIÓN DE TABLAS #############
conexion.execute("""create table if not exists articulos (
                              fecha text,
                              sid integer primary key,
                              msg text,
                              clasification text, 
                              prioridad integer,
                              protocolo text,
                              origen text, 
                              destino text, 
                              puerto integer
                        )""")
conexion.execute("""create table if not exists dispositivos(
                                  id text,
                                  ip text primary key,
                                  localizacion text,
                                  responsable text,
                                  analisis integer
                            )""")
cursor.execute("""create table if not exists responsables(
                                      name text primary key,
                                      telefono integer,
                                      rol text
                                )""")
cursor.execute("""create table if not exists analisis(
                                      id integer,
                                      puertos_abiertos text,
                                      n_puertos_abiertos integer,
                                      servicios integer,
                                      servicios_inseguros integer,
                                      vulnerabilidades_detectadas integer,
                                      primary key(puertos_abiertos, n_puertos_abiertos, servicios, servicios_inseguros, vulnerabilidades_detectadas)
                                )""")

############## RELLENAR TABLAS #############################3

analisis_id = 0
for a in devices:
        responsable = a['responsable']
        cursor.execute("INSERT OR IGNORE INTO responsables (name,telefono,rol) VALUES(?,?,?)", (responsable['nombre'], responsable['telefono'], responsable['rol']))
        analisis = a['analisis']
        if analisis["puertos_abiertos"] == 'None':
            aux = 0
        else:
            aux = len(analisis["puertos_abiertos"])

        cursor.execute("INSERT OR IGNORE INTO analisis (id, puertos_abiertos, n_puertos_abiertos, servicios, servicios_inseguros, vulnerabilidades_detectadas) VALUES(?,?,?,?,?,?)", (analisis_id,json.dumps(analisis['puertos_abiertos']), aux, analisis['servicios'], analisis['servicios_inseguros'], analisis['vulnerabilidades_detectadas']))
        cursor.execute("INSERT OR IGNORE INTO dispositivos (id,ip,localizacion,responsable,analisis) VALUES(?,?,?,?,?)", (a['id'],a['ip'],a['localizacion'],responsable['nombre'],analisis_id))
        ##devices.to_sql("dispositivos", conexion, if_exists="replace", index=False)
        analisis_id+=1


############## SELECCIONES #####################

analisis_analisis = pd.read_sql_query("SELECT * FROM analisis", conexion)

data.to_sql("articulos", conexion, if_exists="replace", index=False)
cursor.execute("SELECT COUNT(*) FROM dispositivos")
n_dispositivos = cursor.fetchone()
print(n_dispositivos[0])
cursor.execute("SELECT COUNT(*) FROM articulos")
n_alertas = cursor.fetchone()
print(n_alertas[0])

cursor.execute("SELECT AVG(n_puertos_abiertos) FROM analisis")
media_abiertos= cursor.fetchone()
##cursor.execute("SELECT STDEV(n_puertos_abiertos) FROM analisis")
print("{:.2f}".format(media_abiertos[0]), "{:.2f}".format(analisis_analisis['n_puertos_abiertos'].std()))

cursor.execute("SELECT AVG(servicios_inseguros) FROM analisis")
media_inseguros= cursor.fetchone()
##cursor.execute("SELECT STDEV(servicios_inseguros) FROM analisis")
print("{:.2f}".format(media_inseguros[0]),"{:.2f}".format(analisis_analisis['servicios_inseguros'].std()))

cursor.execute("SELECT AVG(vulnerabilidades_detectadas) FROM analisis")
media_vulnerabilidades= cursor.fetchone()
##cursor.execute("SELECT STDEV(vulnerabilidades_detectadas) FROM analisis")
print("{:.2f}".format(media_vulnerabilidades[0]),"{:.2f}".format(analisis_analisis['vulnerabilidades_detectadas'].std()))

cursor.execute("SELECT max(n_puertos_abiertos) FROM analisis")
max_abiertos= cursor.fetchone()
cursor.execute("SELECT min(n_puertos_abiertos) FROM analisis")
min_abiertos= cursor.fetchone()
print(max_abiertos[0],min_abiertos[0])

cursor.execute("SELECT max(vulnerabilidades_detectadas) FROM analisis")
max_vuln= cursor.fetchone()
cursor.execute("SELECT min(vulnerabilidades_detectadas) FROM analisis")
min_vuln= cursor.fetchone()
print(max_vuln[0],min_vuln[0])






conexion.close()
