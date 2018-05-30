#!/usr/bin/python
import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import mysql.connector



def executeSQL(db, id):
    cursor = db.cursor()
    try:
        query = "DELETE FROM permisos WHERE id_tarjeta=" + str(id)
        cursor.execute(query)
        db.commit()
        return 1
    except:
        db.rollback()
        return 0


# Aqui empieza lo bueno 
connection = mysql.connector.connect( host='localhost', user='root', passwd='', db='datos_iot' )
reader = SimpleMFRC522.SimpleMFRC522()

try:
  print("Por Favor Deslisa la Tarjeta")
  id,text = reader.read()
  time.sleep(0.2)
  exito = executeSQL(connection, id)
  connection.close()
  if(exito > 0):
    print("\n \n")
    print("-----------------------")
    print(" eliminado")
    print("----------------------")
    print("\n")
    print('Usuario: ' + text)
    print('ID de tarjeta: ' + str(id))
  else:
    print("\n ")
    print(" neh ")
    print('No esta registrado: '+ text)
    print('ID de tarjeta: ' + str(id))
finally:
  print('\n')