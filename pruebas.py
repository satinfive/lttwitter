# -*- coding: utf-8 -*-
import tweepy
import sys
import codecs
sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
import re
from datetime import datetime #Para saber la fecha actual
from geopy.geocoders import Nominatim
import googlemaps


CONSUMER_KEY='a7MAY0h48FEvXSLGY1feZmAnQ'
CONSUMER_SECRET='ybIQ6NETGDY3BkNxSE33kudLAe3Ne9QV32BZOULYrXTBUKF00Y'
ACCESS_TOKEN='4927389436-DQoTWqAHCycPmfRHQ6S9RLRlkQhxzoAoIcNBuaj'
ACCESS_TOKEN_SECRET='2gg3cx00WHe9ZEKYJ5nkgTIt2pQZIXizuX1Nwuh6rGAcT'

API_GOOGLE='AIzaSyCJDjzEL1L92RoVKJ4UooxzhGrYgKH9edQ'

auth= tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api=tweepy.API(auth)

usuario=api.get_user(screen_name='_ill0')

def prueba():
    tweets=[]

    gmaps=googlemaps.Client(key=API_GOOGLE)

    consultaV=api.user_timeline(id=usuario.id, count=100, max_id=717894918967009280)
    direcciones=[]
    for tweet in consultaV:
        if tweet.coordinates!=None:
            latitud, longitud=(str(tweet.coordinates["coordinates"][0]),str(tweet.coordinates["coordinates"][1]) )
            coordenadas=longitud+", "+latitud
            direccion = gmaps.reverse_geocode((float(longitud), float(latitud)))
            #m=re.match(".*,\s(.*),\sProvincia\sde\s(.*)",direccion)
            #print (m.group(2).split(","))[0]
            #print m.group(1)
            direcciones.append(direccion)
        print tweet.id

        tweets.append(tweet)

    return tweets, direcciones


direcciones=prueba()[1]


for el in direcciones[0][0]["address_components"]:
    if "locality" in el["types"] or "administrative_area_level_2" in el["types"]:
        print el["long_name"]
