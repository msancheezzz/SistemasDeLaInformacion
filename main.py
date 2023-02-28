import sqlite3

conexion=sqlite3.connect("bd1.db")
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

conexion.execute("insert into articulos(fecha, sid, msg, clasification, prioridad, protocolo, origen, destino, puerto) values(?,?, ?, ?, ?, ?, ?, ?, ?)", ("2022-07-03 00:19:55",2402000,"ET DROP Dshield Block Listed Source group 1","Misc Attack",2,"UDP","146.88.240.0","172.19.0.0",1194))
conexion.commit()

cursor=conexion.execute("select codigo,msg from articulos")
for fila in cursor:
    print(fila)


conexion.close()