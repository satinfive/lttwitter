# -*- coding: utf-8 -*-
from datos.extraccion import extraer_opiniones, extraer_followers
from modelos import Usuario



def datosLimpios(hashtags, evento):

    def extraer_coordenadas(usuario, localizaciones):

        coordenadas=localizaciones[usuario]
        if not coordenadas:
            return None
        else:
            return coordenadas

    def extraer_localizacion_real(usuario, localizaciones):
        try:
            localizacion=localizaciones[usuario.id_str]
        except KeyError:
            localizacion=()

        if not localizacion:
            localizacion=usuario.location if usuario.location!=None else None
        else:
            localizacion=localizacion[0]


        return localizacion



    usuarios=[]
    for hashtag in hashtags:

        tweets=extraer_opiniones(hashtag)
        aux=[Usuario(raw=tweet.author, name=tweet.author.screen_name, interaction=[(1, tw.id_str) for tw in tweets if tw.author.screen_name==tweet.author.screen_name], evento=evento, busqueda=hashtag, id=tweet.author.id_str, coordinates=(str(tweet.coordinates["coordinates"][1])+", "+str(tweet.coordinates["coordinates"][0]) ) if tweet.coordinates!=None else None, description=tweet.author.description if tweet.author.description!=None else None, located=tweet.author.location if tweet.author.location!=None else None, timeline=True) for tweet in tweets]
        usuarios.extend(aux)


    usuariosNoRepetidos=set(usuarios)

    usuarios=list(usuariosNoRepetidos)

    return usuarios

def get_seguidores(usuario):

    seguidoresSucio=extraer_followers(usuario)

    return [Usuario(raw=user, name=user.screen_name, interaction=None, evento=None, busqueda=None, id=user.id, coordinates=None, description=user.description if user.description!=None else None, located=user.location if user.location!=None else None, timeline=True) for user in seguidoresSucio]

#print get_seguidores('tenjanuary')