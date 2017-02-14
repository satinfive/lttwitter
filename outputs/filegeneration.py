from datos import almacenamiento
import os
from datetime import datetime
import re

DIRBASE="C:/Users/satos/Dropbox/LT CoWorking/Web Development/DALILA/CSV's de Twitter/"
FECHAACTUAL=re.match("(.+)\s(.*):(.*):(.*)..*",str(datetime.now()))

def genera_archivo_txt(evento):
    datos= almacenamiento.extraeTodosDatos(evento)
    datos.insert(0,"Username;Localizacion;Bio;Coordenadas;InteraccionesPorBusqueda;Interacciones;Evento;Busqueda;FechaUltimoTweet;Seguidores;Seguidos;NumTweets")

    evento=datos[1].split(";")[6]

    path=DIRBASE+"EVENTOS/"+evento+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()


def genera_archivo_followers(usuario):

    datosBrutos=almacenamiento.extrae_seguidores(usuario)

    datos=[';'.join(fila) for fila in datosBrutos]

    #datos.insert(0, "Username;Localizacion;Bio;SeguidorDe")
    datos.insert(0, "Username;Localizacion;Bio;SeguidorDe;FechaUltimoTweet;Seguidores;Seguidos;NumeroTweets")

    followersUsuario=datos[1].split(";")[3]

    path=DIRBASE+"FOLLOWERS/"+"Followers de "+followersUsuario+"_"+FECHAACTUAL.group(1)+".csv"
    f = open(path, 'w')
    f.writelines(line.encode('utf8')+"\n" for line in datos)
    f.close()



