import sqlite3
import pandas as pd

data = pd.read_csv("Data/alerts.csv")

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
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
finally:
    data.to_sql("articulos", conexion, if_exists="replace", index=False)

    cursor = conexion.execute("select sid, msg, puerto from articulos")
    for fila in cursor:
        print(fila)

    conexion.close()
