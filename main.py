import sqlite3

conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio integer
                        )""")
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")

conexion.execute("insert into articulos(descripcion, precio) values(?,?)", ("tetongas", 2))
conexion.commit()

cursor=conexion.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(fila)


conexion.close()