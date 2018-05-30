#!/usr/bin/python

import SimpleMFRC522
import time
import mysql.connector

hostname = 'localhost'
username = 'root'
password = ''
database = 'datos_iot'

reader = SimpleMFRC522.SimpleMFRC522()

def executeSQL(conn, clave):
    # print('entra la funcion db')
    cursor = conn.cursor()
    query = "SELECT  id_usr FROM testeo WHERE clave='" + clave+ "'"
    cursor.execute(query)
    result = cursor.fetchall() 
    # print(result)
    if(result):   
        return result[0][0]
    else:
        return 0

# Aqui empieza lo bueno 
connection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )

try:
  print("Por Favor Deslisa la Tarjeta")
  id,text = reader.read()
  time.sleep(0.2)
  nvt = text.split(' ')[0]
  exito = executeSQL(connection, nvt)
  connection.close()
  #print(text)
  if(exito > 0):
    print("\n \n")
    print("-----------------------")
    print(" B I E N V E N I D O ")
    print("----------------------")
    print("\n")
    print('Id Usuario: ' + nvt)
    print('ID de tarjeta: ' + str(id))
  else:
    print("\n \n")
    print(" Acceso denegado ")
    print("----------------------")
    print('No esta registrado: '+ nvt )
    print('ID de tarjeta: ' + str(id))
finally:
  print('\n')



    
    

