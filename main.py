import json
import sqlite3
import pandas as pd

data = pd.read_csv("Data/alerts.csv")
dev = open("data/devices.json")
devices = json.load(dev)


rows = data.shape[0]
conexion = sqlite3.connect("bd1.db")
cursor = conexion.cursor()


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


data.to_sql("articulos", conexion, if_exists="replace", index=False)
cursor.execute("SELECT COUNT(*) FROM dispositivos")
n_dispositivos = cursor.fetchone()
print(n_dispositivos)
cursor.execute("SELECT COUNT(*) FROM articulos")
n_alertas = cursor.fetchone()
print(n_alertas)
cursor.execute("SELECT AVG(n_puertos_abiertos) FROM analisis")
media_abiertos= cursor.fetchone()
cursor.execute("SELECT STDEV(n_puertos_abiertos) FROM analisis")
desviacion_abiertos= cursor.fetchone()
print(media_abiertos)





conexion.close()
