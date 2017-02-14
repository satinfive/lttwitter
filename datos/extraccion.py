import tweepy
import sys
import codecs
sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
import re
from datetime import datetime #Para saber la fecha actual
import googlemaps
from operator import itemgetter
from time import sleep


CONSUMER_KEY='a7MAY0h48FEvXSLGY1feZmAnQ'
CONSUMER_SECRET='ybIQ6NETGDY3BkNxSE33kudLAe3Ne9QV32BZOULYrXTBUKF00Y'
ACCESS_TOKEN='4927389436-DQoTWqAHCycPmfRHQ6S9RLRlkQhxzoAoIcNBuaj'
ACCESS_TOKEN_SECRET='2gg3cx00WHe9ZEKYJ5nkgTIt2pQZIXizuX1Nwuh6rGAcT'

API_GOOGLE='AIzaSyCJDjzEL1L92RoVKJ4UooxzhGrYgKH9edQ'

AUTH= tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def extraer_opiniones(hashtag, fecha=datetime.now()):

    tweets=[]
    localizaciones=dict()

    if isinstance(fecha, datetime):
        fechaActual=str(fecha)
        mesConsiderado=(re.match("\d{4}-(\d{2})-\d{2}\s.*", fechaActual)).group(1)
    else:
        mesConsiderado=fecha


    def consulta(hashtag, max_id=None):


            if max_id==None:
                consultaV=api.search(q=hashtag,count=100, show_user=True, lang='es', result_type="recent", wait_on_rate_limit=True)

            else:
                consultaV=api.search(q=hashtag, count=100, show_user=True, lang='es', result_type="recent", max_id=max_id, wait_on_rate_limit=True)


            return consultaV

    def obtener_localizacion(usuario_id, coordenadas):

        primerTweet=api.user_timeline(id=usuario_id, count=1)[0]
        idTweet=primerTweet.id

        print api.get_user(id=usuario_id).screen_name

        gmaps=googlemaps.Client(key=API_GOOGLE)

        direcciones={}

        while(True):

            usuario_timeline=api.user_timeline(id=usuario_id, count=100, max_id=idTweet)

            for tweet in usuario_timeline:

                if tweet.coordinates!=None and tweet.coordinates!=coordenadas:
                    latitud, longitud=(str(tweet.coordinates["coordinates"][0]),str(tweet.coordinates["coordinates"][1]) )
                    coordenadas=longitud+", "+latitud

                    if coordenadas in direcciones.values():
                        clave=[(dire, coor) for dire, coor in direcciones.items() if coor==coordenadas][0]
                        direcciones[clave]=direcciones[clave]+1
                        if direcciones[clave]>5:
                            return clave

                    else:
                        direRaw=gmaps.reverse_geocode((float(longitud), float(latitud)))
                        direCorta=[el["long_name"] for el in direRaw[0]["address_components"] if "locality" in el["types"] or "administrative_area_level_2" in el["types"]]
                        direccion=(", ").join(direCorta)
                        direcciones[(direccion,coordenadas)]=1



            if len(usuario_timeline) <=1:
                break

            idTweet=usuario_timeline[len(usuario_timeline)-1].id

        if not direcciones:
            return ()
        else:
            #conteo=Counter(direccion for direccion,_ in direcciones)
            return max(direcciones.items(), key=itemgetter(1))



    resultado=consulta(hashtag)
    for tweet in resultado:
        print tweet.text
        print tweet.author.screen_name
        tweets.append(tweet)



    if tweets:
        idUltimoTweet=tweets[len(tweets)-1].id_str
        fechaUltimoTweet=str(api.get_status(idUltimoTweet).created_at)
        mesUltimoTweet=(re.match("\d{4}-(\d{2})-\d{2}\s.*",fechaUltimoTweet)).group(1)

        #sleep(30)
    else:
        return tweets

    idAntiguo=""

    while(True):
        resultado=consulta(hashtag, max_id=idUltimoTweet)

        for tweet in resultado:
            print tweet.text
            print tweet.author.screen_name
            tweets.append(tweet)

        if idAntiguo == idUltimoTweet:
            break

        if tweets:
            idAntiguo=idUltimoTweet
            idUltimoTweet=tweets[len(tweets)-1].id_str
            fechaUltimoTweet=str(api.get_status(idUltimoTweet).created_at)
            mesUltimoTweet=(re.match("\d{4}-(\d{2})-\d{2}\s.*",fechaUltimoTweet)).group(1)
            #sleep(30)
        else:
            break

    return tweets


def extraer_followers(usuario):

    seguidores=[]

    followers= tweepy.Cursor(api.followers, screen_name=usuario, count=200, wait_on_rate_limit=True).items()


    for usuario in followers:
        seguidores.append(usuario)

    return seguidores



api=tweepy.API(AUTH)







