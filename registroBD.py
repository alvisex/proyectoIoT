#!/usr/bin/python

import SimpleMFRC522
import time
import mysql.connector
import RPi.GPIO as GPIO

def executeSQL(db, clave, usuario):
    # print('entra la funcion db')
    cursor = db.cursor()
    try:
        query = "INSERT INTO permisos VALUES (" + str(clave) + ", '" + str(usuario) + "', 1);"
        cursor.execute(query)
        # cursor.execute ("""INSERT INTO mutual_funds (mf_id, mf_name, mf_nav, mf_nav_dt) VALUES (%s, %s, %l, %s)""", (120523,"Axis Fund",14.6357,88888))
        db.commit()
        return 1
    except db.Error as error:
        print("Error: {}".format(error))
        db.rollback()
        return 0




# Aqui empieza lo bueno 
reader = SimpleMFRC522.SimpleMFRC522()
connection = mysql.connector.connect( host='localhost', user='root', passwd='', db='datos_iot' )


try:
  text = raw_input('Nombre del nuevo usuario:')
  print("Acerca tu tarjeta hasta que se te indique")
  reader.write(text)
  time.sleep(0.2)
  id,text = reader.read()
  time.sleep(0.2)
  exito = executeSQL(connection, id, text)
  connection.close()
  if(exito):
    print("\n \n")
    print("-----------------------")
    print(" R E G  I S T R D A D O ")
    print("----------------------")
    print("\n")
    print('Usuario: ' + text)
    print('ID de tarjeta: ' + str(id))
  else:
    print("\n \n")
    print(" NOPE ")
    print('No esta registrado: '+ text)
    print('ID de tarjeta: ' + str(id))
finally:
    GPIO.cleanup()