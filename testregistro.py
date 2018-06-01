#!/usr/bin/python
import time
import mysql.connector
import datetime

hostname = 'localhost'
username = 'root'
password = ''
database = 'iot'


def executeSQL(conn, clave):
    # print('entra la funcion db')
    cursor = conn.cursor()
    query = "SELECT permiso FROM permisos WHERE id_tarjeta=" + str(clave)
    cursor.execute(query)
    result = cursor.fetchall() 
    print(result)
    if(result):   
        return result[0][0]
        #return 1
    else:
        return 0

def registroBD(db, clave, usuario):
    # print('entra la funcion db')
    cursor = db.cursor()
    try:
        now = datetime.datetime.now()
        query = "INSERT INTO registro VALUES (" + str(clave) + ", '" + str(usuario) + "', '"+ str(now) +"');"
        cursor.execute(query)
        db.commit()
        return 1
    except db.Error as error:
        print("Error: {}".format(error))
        db.rollback()
        return 0

def acceso():
    print("\n \n")
    print("-----------------------")
    print(" B I E N V E N I D O ")
    print("----------------------")
    print("\n")
    print('Usuario: ' + text)
    print('ID de tarjeta: ' + str(id))


# Aqui empieza lo bueno 
connection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )

try:
  print("Por Favor Deslisa la Tarjeta")
  id = 123123123
  text = 'holaaaa'
  time.sleep(0.2)
  #nvt = text.split(' ')[0]         Obtener texto sin espacion en blanco
  exito = executeSQL(connection, id)
  
  #print(text)
  if(exito > 0):
    if (registroBD(connection, id, text)):
        print("Registrado exitosamente")
    acceso()
  else:
    print("\n \n")
    print(" Acceso denegado ")
    print("----------------------")
    print('No esta registrado: '+ text)
    print('ID de tarjeta: ' + str(id))
finally:
    connection.close()
    print('\n')