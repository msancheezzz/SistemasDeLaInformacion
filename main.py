import pprint
import sqlite3
import pandas as pd

data = pd.read_csv("Data/alerts.csv")
devices = pd.read_json("Data/devices.json")

rows = data.shape[0]
conexion = sqlite3.connect("bd1.db")

try:
    conexion.execute("""create table articulos (
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
    conexion.execute("""create table dispositivos (
                                  name text,
                                  ip integer primary key,
                                  localizacion text,
                                  responsable text foreign key,
                                  analisis text foreign key
                            )""")
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
finally:
    data.to_sql("articulos", conexion, if_exists="replace", index=False)
    ##devices.to_sql("dispositivos", conexion, if_exists="replace", index=False)
    print(devices)

    conexion.close()
