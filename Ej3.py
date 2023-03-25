import json
import sqlite3
import pandas as pd
import matplotlib as mp

###### CONEXIONES Y FICHEROS #########
conexion = sqlite3.connect("bd1.db")
cursor = conexion.cursor()

vulnerabilidadesPrioridad = pd.read_sql_query("SELECT aux1.prioridad, aux2.vulnerabilidades_detectadas, aux2.ip from analisis aux2 JOIN (SELECT prioridad, origen, destino FROM articulos) aux1 ON aux1.origen=aux2.ip OR aux1.destino=aux2.ip WHERE aux1.prioridad=1;", conexion)
print("Número de vulnerabilidades de prioridad 1:",len(vulnerabilidadesPrioridad.index))
print("Media de vulnerabilidades de prioridad 1:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].mean())
print("Mediana de vulnerabilidades de prioridad 1:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].median())
print("Varianza de vulnerabilidades de prioridad 1:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].var())
print("Máximo de vulnerabilidades de prioridad 1:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].max())
print("Mínimo de vulnerabilidades de prioridad 1:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].min())

vulnerabilidadesPrioridad = pd.read_sql_query("SELECT aux1.prioridad, aux2.vulnerabilidades_detectadas, aux2.ip from analisis aux2 JOIN (SELECT prioridad, origen, destino FROM articulos) aux1 ON aux1.origen=aux2.ip OR aux1.destino=aux2.ip WHERE aux1.prioridad=2;", conexion)
print("Número de vulnerabilidades de prioridad 2:",len(vulnerabilidadesPrioridad.index))
print("Media de vulnerabilidades de prioridad 2:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].mean())
print("Mediana de vulnerabilidades de prioridad 2:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].median())
print("Varianza de vulnerabilidades de prioridad 2:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].var())
print("Máximo de vulnerabilidades de prioridad 2:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].max())
print("Mínimo de vulnerabilidades de prioridad 2:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].min())

vulnerabilidadesPrioridad = pd.read_sql_query("SELECT aux1.prioridad, aux2.vulnerabilidades_detectadas, aux2.ip from analisis aux2 JOIN (SELECT prioridad, origen, destino FROM articulos) aux1 ON aux1.origen=aux2.ip OR aux1.destino=aux2.ip WHERE aux1.prioridad=3;", conexion)
print("Número de vulnerabilidades de prioridad 3:",len(vulnerabilidadesPrioridad.index))
print("Media de vulnerabilidades de prioridad 3:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].mean())
print("Mediana de vulnerabilidades de prioridad 3:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].median())
print("Varianza de vulnerabilidades de prioridad 3:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].var())
print("Máximo de vulnerabilidades de prioridad 3:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].max())
print("Mínimo de vulnerabilidades de prioridad 3:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].min())

vulnerabilidadesPrioridad = pd.read_sql_query("SELECT aux1.timestamp, aux2.vulnerabilidades_detectadas, aux2.ip from analisis aux2 JOIN (SELECT timestamp, origen, destino FROM articulos) aux1 ON aux1.origen=aux2.ip OR aux1.destino=aux2.ip WHERE aux1.timestamp BETWEEN '2022-06-30' AND '2022-08-01';", conexion)
print("Número de vulnerabilidades en Julio:",len(vulnerabilidadesPrioridad.index))
print("Media de vulnerabilidades en Julio:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].mean())
print("Mediana de vulnerabilidades en Julio:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].median())
print("Varianza de vulnerabilidades en Julio:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].var())
print("Máximo de vulnerabilidades en Julio:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].max())
print("Mínimo de vulnerabilidades en Julio:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].min())

vulnerabilidadesPrioridad = pd.read_sql_query("SELECT aux1.timestamp, aux2.vulnerabilidades_detectadas, aux2.ip from analisis aux2 JOIN (SELECT timestamp, origen, destino FROM articulos) aux1 ON aux1.origen=aux2.ip OR aux1.destino=aux2.ip WHERE aux1.timestamp BETWEEN '2022-07-31' AND '2022-09-01';", conexion)
print("Número de vulnerabilidades en Agosto:",len(vulnerabilidadesPrioridad.index))
print("Media de vulnerabilidades en Agosto:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].mean())
print("Mediana de vulnerabilidades en Agosto:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].median())
print("Varianza de vulnerabilidades en Agosto:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].var())
print("Máximo de vulnerabilidades en Agosto:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].max())
print("Mínimo de vulnerabilidades en Agosto:",vulnerabilidadesPrioridad['vulnerabilidades_detectadas'].min())
