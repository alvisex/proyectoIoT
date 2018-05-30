#!/usr/bin/python
import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import mysql.connector

hostname = 'localhost'
username = 'root'
password = ''
database = 'datos_iot'

reader = SimpleMFRC522.SimpleMFRC522()

def executeSQL(conn, clave):
    cursor = conn.cursor()
    query = "SELECT id_tarjeta FROM permisos WHERE id_tarjeta=" + str(clave)
    cursor.execute(query)
    result = cursor.fetchall() 
    if(result):   
        return result[0][0]
        #return 1
    else:
        return 0

# Aqui empieza lo bueno 
connection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )

try:
  print("Por Favor Deslisa la Tarjeta")
  id,text = reader.read()
  time.sleep(0.2)
  #nvt = text.split(' ')[0]         Obtener texto sin espacion en blanco
  exito = executeSQL(connection, id)
  connection.close()
  #print(text)
  if(exito > 0):
    print("\n Tarjeta registrada \n")
    print('Usuario: ' + text)
    print('ID de tarjeta: ' + str(id))
  else:
    print("\n")
    print('No esta registrado: '+ text)
    print('ID de tarjeta: ' + str(id))
finally:
  print('\n')