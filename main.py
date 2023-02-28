import sqlite3
import pandas as pd

data = pd.read_csv("Data/alerts.csv")
rows = data.shape[0]
conexion = sqlite3.connect("bd1.db")
conexion.execute("drop table articulos")

try:
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              fecha text,
                              sid integer,
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
    for i in range(100):
        conexion.execute("insert into articulos(descripcion, precio) values(?, ?)",(str(data["msg"].iloc[i]), str(data["sid"].iloc[i])))
        conexion.commit()

    cursor = conexion.execute("select codigo,descripcion,precio from articulos")
    for fila in cursor:
        print(fila)

    conexion.close()
