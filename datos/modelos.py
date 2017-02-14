# -*- coding: utf-8 -*-

class Usuario(object):

    def __init__(self, raw, name, interaction, evento, busqueda, id, coordinates=None, description=None, located=None, timeline=False):

        self.raw = raw
        self.username=name
        self.localizacion=located
        self.bio=description
        self.coordenadas=coordinates
        self.interaccionEvento=interaction
        self.evento=evento
        self.busqueda=busqueda
        self.id=id

        if timeline:

            from extraccion import AUTH
            import tweepy

            api = tweepy.API(AUTH)

            try:
                timeline = api.user_timeline(id=self.id, wait_on_rate_limit=True)
            except tweepy.error.TweepError:
                timeline = []

            self.timeline = timeline

            #Esto era para la extraccion de un monton de tweets
            '''from extraccion import AUTH
            import tweepy

            api = tweepy.API(AUTH)

            from datetime import datetime
            from datetime import timedelta

            hoy = datetime.now()
            restasemana = timedelta(days=7)
            semanapasada = hoy - restasemana

            tweetsMes = []

            timelineMes = api.user_timeline(id=self.id, since=semanapasada.date(), until=hoy.date(),
                                        wait_on_rate_limit=True, count=100)

            tweetsMes = [tweet for tweet in timelineMes]

            idUltTweet = timelineMes.max_id

            while True:

                aux = api.user_timeline(id=self.id, max_id=idUltTweet, count=100,
                                        wait_on_rate_limit=True)

                if not aux:
                    break

                fechaulttweet = aux[len(aux)-1].created_at

                if fechaulttweet.month == semanapasada.month and fechaulttweet.day < semanapasada.day:
                    break

                auxMes = [tweet for tweet in aux]
                tweetsMes.extend(auxMes)
                idUltTweet = aux.max_id

            if len(tweetsMes) >= 100:
                self.timeline = tweetsMes
            else:
                tam = len(tweetsMes)
                hastaCien = 100 - tam
                idUltimoTweet = timelineMes[tam-1].id_str
                auxCien = api.user_timeline(id=self.id, count=hastaCien, max_id=idUltimoTweet)
                tweetsCien = [tweet for tweet in auxCien]
                tweetsMes.extend(tweetsCien)
                self.timeline=tweetsMes'''

    def __str__(self):
        return self.username

    def __eq__(self, other):
        return self.username == other.username

    def __hash__(self):

        return hash(self.username)

    def fecha_ultimo_tweet(self):

        if self.timeline:
            ulttweet = self.timeline[0]
            fecha = ulttweet.created_at
        else:
            fecha = "-"

        return fecha

    def numero_seguidores(self):

        return self.raw.followers_count

    def numero_amigos(self):

        return self.raw.friends_count

    def numero_tweets(self):

        return self.raw.statuses_count

    '''def numero_tweets_ultimasemana(self):

        def comprueba_si_retweet(t):

            try:
                t.retweeted_status
                return False
            except AttributeError:
                return True

        from datetime import timedelta
        from datetime import datetime

        hoy = datetime.now()
        restasemana = timedelta(days=7)
        semanapasada = hoy - restasemana

        return len([tweet for tweet in self.timeline if tweet.created_at >= semanapasada and comprueba_si_retweet(tweet)])

    def numero_retweets_por_cien_tweets(self):

        cientweets = self.timeline[:100]

        return sum((tweet.retweet_count for tweet in cientweets))/100.0

    def numero_favs_por_cien_tweets(self):

        cientweets = self.timeline[:100]

        return sum((tweet.favorite_count for tweet in cientweets))/100.0'''













