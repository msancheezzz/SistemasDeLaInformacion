import json
import sqlite3
import pandas as pd

data = pd.read_csv("Data/alerts.csv")
dev = open("data/devices.json")
devices = json.load(dev)


rows = data.shape[0]
conexion = sqlite3.connect("bd1.db")
cursor = conexion.cursor()

##try:
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
                                  name text,
                                  ip text primary key,
                                  localizacion text,
                                  responsable text,
                                  analisis integer
                            )""")
conexion.execute("""create table if not exists responsables(
                                      name text primary key,
                                      telefono integer,
                                      rol text
                                )""")
conexion.execute("""create table if not exists analisis(
                                      id integer primary key,
                                      puertos_abiertos text,
                                      n_puertos_abiertos integer,
                                      servicios integer,
                                      servicios_inseguros integer,
                                      vulnerabilidades_detectadas integer
                                )""")
"""except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
finally:"""
data.to_sql("articulos", conexion, if_exists="replace", index=False)
for a in devices:
        responsable = a['responsable']
        cursor.execute("INSERT OR IGNORE INTO responsables (name,telefono,rol) VALUES(?,?,?)", (responsable['nombre'], responsable['telefono'], responsable['rol']))
        analisis = a['analisis']
        if analisis["puertos_abiertos"] == 'None':
            aux = 0
        else:
            aux = len(analisis["puertos_abiertos"])
        cursor.execute("INSERT OR IGNORE INTO analisis (puertos_abiertos, n_puertos_abiertos, servicios, servicios_inseguros, vulnerabilidades_detectadas) VALUES(?,?,?,?,?)", (json.dumps(analisis['puertos_abiertos']), aux, analisis['servicios'], analisis['servicios_inseguros'], analisis['vulnerabilidades_detectadas']))
        analisis_id = cursor.lastrowid
        cursor.execute("INSERT OR IGNORE INTO dispositivos (name) VALUES(?)", (a['id']))
        ##devices.to_sql("dispositivos", conexion, if_exists="replace", index=False)
print(devices)

conexion.close()
