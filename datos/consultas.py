# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
import re

CONEXION=None
DIRBASE="C:/Users/satos/Dropbox/LT CoWorking/Web Development/DALILA/CSV's de Twitter/"
FECHAACTUAL=re.match("(.+)\s(.*):(.*):(.*)..*",str(datetime.now()))

def conectarBD():

    conn=sqlite3.connect('C:\Users\satos\PycharmProjects\LTPruebaTwitter\datos.db')

    return conn

def limpia_eventos():

    cursor=CONEXION.execute("DELETE FROM USUARIOS WHERE interaccionevento=0")


def username_usuarios(user):

    limpia_eventos()

    cursor=CONEXION.execute("SELECT * FROM USUARIOS WHERE username LIKE '%"+user+"%'")

    datosBrutos = [(row[1],row[2].replace("None",''), ((row[3].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "", row[4].replace("None",''), str(row[5]), str(row[6]), row[7], row[8]) for row in cursor]

    datos=[';'.join(fila) for fila in datosBrutos]
    datos.insert(0, "Username;Localizacion;Bio;Coordenadas;InteraccionesPorBusqueda;Interacciones;Evento;Busqueda")
    path=DIRBASE+"EVENTOS/"+"Consulta de username = "+user+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()

def localizacion_usuarios(loc):

    limpia_eventos()

    cursor=CONEXION.execute("SELECT * FROM USUARIOS WHERE localizacion LIKE '%"+loc+"%'")

    datosBrutos = [(row[1],row[2].replace("None",''), ((row[3].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "", row[4].replace("None",''), str(row[5]), str(row[6]), row[7], row[8]) for row in cursor]

    datos=[';'.join(fila) for fila in datosBrutos]
    datos.insert(0, "Username;Localizacion;Bio;Coordenadas;InteraccionesPorBusqueda;Interacciones;Evento;Busqueda")
    path=DIRBASE+"EVENTOS/"+"Consulta de localizacion = "+loc+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()

def bio_usuarios(bi):

    limpia_eventos()

    cursor=CONEXION.execute("SELECT * FROM USUARIOS WHERE bio LIKE '%"+bi+"%'")

    datosBrutos = [(row[1],row[2].replace("None",''), ((row[3].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "", row[4].replace("None",''), str(row[5]), str(row[6]), row[7], row[8]) for row in cursor]

    datos=[';'.join(fila) for fila in datosBrutos]
    datos.insert(0, "Username;Localizacion;Bio;Coordenadas;InteraccionesPorBusqueda;Interacciones;Evento;Busqueda")
    path=DIRBASE+"EVENTOS/"+"Consulta de biografia = "+bi+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()

def intercevento_usuarios(num):

    limpia_eventos()

    cursor=CONEXION.execute("SELECT * FROM USUARIOS WHERE interaccionevento LIKE '%"+num+"%'")

    datosBrutos = [(row[1],row[2].replace("None",''), ((row[3].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "", row[4].replace("None",''), str(row[5]), str(row[6]), row[7], row[8]) for row in cursor]

    datos=[';'.join(fila) for fila in datosBrutos]
    datos.insert(0, "Username;Localizacion;Bio;Coordenadas;InteraccionesPorBusqueda;Interacciones;Evento;Busqueda")
    path=DIRBASE+"EVENTOS/"+"Consulta de interaccion de eventos = "+num+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()

def evento_usuarios(ev):

    limpia_eventos()

    cursor=CONEXION.execute("SELECT * FROM USUARIOS WHERE evento LIKE '%"+ev+"%'")

    datosBrutos = [(row[1],row[2].replace("None", ''), ((row[3].replace("\n", '')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "", row[4].replace("None",''), str(row[5]), str(row[6]), row[7], row[8]) for row in cursor]

    datos=[';'.join(fila) for fila in datosBrutos]
    datos.insert(0, "Username;Localizacion;Bio;Coordenadas;InteraccionesPorBusqueda;Interacciones;Evento;Busqueda")
    path=DIRBASE+"EVENTOS/"+"Consulta de eventos = "+ev+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()

def busqueda_usuarios(busq):

    limpia_eventos()

    cursor=CONEXION.execute("SELECT * FROM USUARIOS WHERE busqueda LIKE '%"+busq+"%'")

    datosBrutos = [(row[1],row[2].replace("None",''), ((row[3].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "", row[4].replace("None",''), str(row[5]), str(row[6]), row[7], row[8]) for row in cursor]

    datos=[';'.join(fila) for fila in datosBrutos]
    datos.insert(0, "Username;Localizacion;Bio;Coordenadas;InteraccionesPorBusqueda;Interacciones;Evento;Busqueda")
    path=DIRBASE+"EVENTOS/"+"Consulta de busquedas = "+busq+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()

def localizacion_followers(loc):

    cursor=CONEXION.execute("SELECT * FROM FOLLOWERS WHERE localizacion LIKE '%"+loc+"%'")

    datosBrutos =  [(row[0],
             row[1].replace("None", ''),
             ((row[2].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "",
             str(row[3]),
             str(row[4]),
             str(row[5]),
             str(row[6]),
             str(row[7]),
             str(row[8]),
             str(row[9])) for row in cursor]

    datos=[';'.join(fila) for fila in datosBrutos]
    datos.insert(0, "Username;Localizacion;Bio;SeguidorDe;FechaUltimoTweet;NumeroSeguidores;NumeroTweets;NumeroTweetsUltimaSemana;RTPorCienTweets;FAVPorCienTweets")
    path=DIRBASE+"FOLLOWERS/"+"Consulta de localizacion = "+loc+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()

def bio_followers(term):

    cursor=CONEXION.execute("SELECT * FROM FOLLOWERS WHERE bio LIKE '%"+term+"%'")

    datosBrutos =  [(row[0],
             row[1].replace("None", ''),
             ((row[2].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "",
             str(row[3]),
             str(row[4]),
             str(row[5]),
             str(row[6]),
             str(row[7]),
             str(row[8]),
             str(row[9])) for row in cursor]

    datos=[';'.join(fila) for fila in datosBrutos]
    datos.insert(0, "Username;Localizacion;Bio;SeguidorDe;FechaUltimoTweet;NumeroSeguidores;NumeroTweets;NumeroTweetsUltimaSemana;RTPorCienTweets;FAVPorCienTweets")
    path=DIRBASE+"FOLLOWERS/"+"Consulta de bio = "+term+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()

def username_followers(user):

    cursor=CONEXION.execute("SELECT * FROM FOLLOWERS WHERE username LIKE '%"+user+"%'")

    datosBrutos =  [(row[0],
             row[1].replace("None", ''),
             ((row[2].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "",
             str(row[3]),
             str(row[4]),
             str(row[5]),
             str(row[6]),
             str(row[7]),
             str(row[8]),
             str(row[9])) for row in cursor]

    datos=[';'.join(fila) for fila in datosBrutos]
    datos.insert(0, "Username;Localizacion;Bio;SeguidorDe;FechaUltimoTweet;NumeroSeguidores;NumeroTweets;NumeroTweetsUltimaSemana;RTPorCienTweets;FAVPorCienTweets")
    path=DIRBASE+"FOLLOWERS/"+"Consulta de usernames = "+user+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()

def seguidorde_followers(user):

    cursor=CONEXION.execute("SELECT * FROM FOLLOWERS WHERE seguidorde LIKE '%"+user+"%'")

    datosBrutos =  [(row[0],
             row[1].replace("None", ''),
             ((row[2].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "",
             str(row[3]),
             str(row[4]),
             str(row[5]),
             str(row[6]),
             str(row[7]),
             str(row[8]),
             str(row[9])) for row in cursor]

    datos=[';'.join(fila) for fila in datosBrutos]
    datos.insert(0, "Username;Localizacion;Bio;SeguidorDe;FechaUltimoTweet;NumeroSeguidores;NumeroTweets;NumeroTweetsUltimaSemana;RTPorCienTweets;FAVPorCienTweets")
    path=DIRBASE+"FOLLOWERS/"+"Consulta de seguidores de = "+user+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()

CONEXION = conectarBD()

#Para que se ejecute la consulta, descomentar la linea (quitar la almohadilla).
#Sustituye palabra por lo que quieres buscar, pero no quites las comillas.

'''CONSULTAS PARA EVENTOS'''
#Para consultar los usuarios registrados de los eventos.
#username_usuarios("palabra")
#Para consultar la localizacion de los usuarios registrados de los eventos.
#localizacion_usuarios("palabra")
#Para consultar la biografia de los usuarios registrados de los eventos.
#bio_usuarios("anime")
#Para consultar la interaccion de los eventos de los usuarios registrados de los eventos.
#intercevento_usuarios("palabra")
#Para consultar los eventos en donde se han encontrado los usuarios.
#evento_usuarios("palabra")
#Para consultar las palabras con las que se ha encontrado los usuarios.
#busqueda_usuarios("palabra")

'''CONSULTAS PARA FOLLOWERS'''
#Para consultar las localizaciones de usuarios.
#localizacion_followers("palabra")
#Para consultar la biografia de los usuarios.
bio_followers("anime")
#Para consultar el usuario de los que los usuarios son seguidores.
#seguidorde_followers("palabra")
#Para buscar a algun usuario por su username.
#username_followers("palabra")