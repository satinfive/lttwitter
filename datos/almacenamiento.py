import sqlite3
from ast import literal_eval as make_tuple
import limpieza
import sys

CONEXION=None


def seleccionaDatos(ev, hash):

    evento = sys.argv[1]
    h = sys.argv[2]

    hashtags=h.split(",")

    return (hashtags, evento)

def seleccionaUsuarioFollowers():

    usuario=sys.argv[1]

    return usuario

def crearBD():

    conn=sqlite3.connect('C:\Users\satos\PycharmProjects\LTPruebaTwitter\datos.db')

    return conn

def generaBD(conn, borrar=False):
    if borrar:
        conn.execute('drop table if exists USUARIOS')
        conn.execute('DROP TABLE if exists FOLLOWERS')

    conn.execute('''CREATE TABLE IF NOT EXISTS USUARIOS
              (ID INT NOT NULL,
              USERNAME CHAR(100) NOT NULL,
              LOCALIZACION CHAR(100) NULL,
              BIO VARCHAR(1000) NULL,
              COORDENADAS CHAR(100) NULL,
              INTERACCIONPORTWEET VARCHAR(200),
              INTERACCIONEVENTO INTEGER,
              EVENTO CHAR(200),
              BUSQUEDA VARCHAR(500),
              FECHAULTIMOTWEET VARCHAR(100),
              NUMEROSEGUIDORES INTEGER,
              NUMEROAMIGOS INTEGER,
              NUMEROTWEETS INTEGER,
              PRIMARY KEY(USERNAME, EVENTO, BUSQUEDA));''')

    conn.execute('''CREATE TABLE IF NOT EXISTS FOLLOWERS
                    (USERNAME CHAR(100) NOT NULL,
                    LOCALIZACION CHAR(100) NULL,
                    BIO VARCHAR(1000) NULL,
                    SEGUIDORDE CHAR(100),
                    FECHAULTIMOTWEET VARCHAR(100),
                    NUMEROSEGUIDORES INTEGER,
                    NUMEROAMIGOS INTEGER,
                    NUMEROTWEETS INTEGER,
                    PRIMARY  KEY (USERNAME, SEGUIDORDE));''')


def almacenaDatos(conn, evento=False, followers=False, event="", hashtags=[]):

    if followers:
        usuario=seleccionaUsuarioFollowers()
        followers=limpieza.get_seguidores(usuario)

        '''for follower in followers:

            c=conn.execute("SELECT username, seguidorde FROM FOLLOWERS WHERE username='"+follower.username+"' AND seguidorde='"+usuario+"'")

            if len(c.fetchall())==0:
                conn.execute("INSERT INTO FOLLOWERS VALUES (?,?,?,?,?,?,?,?,?,?)",
                             (follower.username,
                              follower.localizacion,
                              follower.bio,
                              usuario,
                              follower.fecha_ultimo_tweet(),
                              str(follower.numero_seguidores(follower)),
                              str(follower.numero_tweets(follower)),
                              str(follower.numero_tweets_ultimasemana()),
                              str(follower.numero_retweets_por_cien_tweets()),
                              str(follower.numero_favs_por_cien_tweets())))

            else:
                continue'''

        for follower in followers:

            c = conn.execute("SELECT username, seguidorde FROM FOLLOWERS WHERE username='"+follower.username+"' AND seguidorde='"+usuario+"'")

            if len(c.fetchall())==0:

                try:
                    print follower.username
                    print follower.numero_seguidores()
                    conn.execute("INSERT INTO FOLLOWERS VALUES (?,?,?,?,?,?,?,?)",
                                 (follower.username,
                                  follower.localizacion,
                                  follower.bio,
                                  usuario,
                                  follower.fecha_ultimo_tweet(),
                                  follower.numero_seguidores(),
                                  follower.numero_amigos(),
                                  follower.numero_tweets()))

                except sqlite3.OperationalError:
                    modifica_followers(CONEXION)

            else:

                c2 = conn.execute("SELECT username, seguidorde FROM FOLLOWERS WHERE username='"+follower.username+"' AND seguidorde='"+usuario+"'")

                for followrow in c2:
                    conn.execute("UPDATE followers SET FECHAULTIMOTWEET='"+str(follower.fecha_ultimo_tweet())+
                                 "', NUMEROSEGUIDORES='"+str(follower.numero_seguidores())+
                                 "', NUMEROAMIGOS='"+str(follower.numero_amigos())+
                                 "', NUMEROTWEETS='"+str(follower.numero_tweets())+
                                 "' WHERE username='"+followrow[0]+"' AND seguidorde='"+followrow[1]+"'")

    if evento:

        (h,e)=seleccionaDatos(event, hashtags)
        usuarios= limpieza.datosLimpios(h, e)
        for usuario in usuarios:
            cursor=conn.execute("SELECT busqueda from USUARIOS WHERE username='"+usuario.username+"' AND evento='"+usuario.evento+"'")
            busquedas=[row[0] for row in cursor]

            if not busquedas:
                if len(cursor.fetchall())==0:
                    try:
                        conn.execute("INSERT INTO USUARIOS VALUES (?, ?, ?, ?,?,?,?, ?, ?, ?, ?, ?, ?)",(usuario.id, usuario.username, usuario.localizacion, usuario.bio,
                                                                            str(usuario.coordenadas), str(usuario.interaccionEvento) ,sum(i for i,_ in usuario.interaccionEvento), usuario.evento, usuario.busqueda, usuario.fecha_ultimo_tweet(), usuario.numero_seguidores(), usuario.numero_amigos(), usuario.numero_tweets()));
                    except sqlite3.IntegrityError:
                        continue
                    except sqlite3.OperationalError:
                        modifica_eventos(CONEXION)

            elif usuario.busqueda in busquedas:
                try:

                    cursor2 = conn.execute("SELECT busqueda from USUARIOS WHERE username='"+usuario.username+"' AND evento='"+usuario.evento+"'")

                    for followrow in cursor2:
                        conn.execute("UPDATE usuarios SET FECHAULTIMOTWEET='"+str(usuario.fecha_ultimo_tweet())+
                                     "', NUMEROSEGUIDORES='"+str(usuario.numero_seguidores())+
                                     "', NUMEROAMIGOS='"+str(usuario.numero_amigos())+
                                     "', NUMEROTWEETS='"+str(usuario.numero_tweets())+
                                     "' WHERE username='"+usuario.username+"' AND evento='"+usuario.evento+"'")

                except sqlite3.OperationalError:
                    modifica_eventos(CONEXION)

            else:
                cursor2=conn.execute("SELECT interaccionportweet FROM USUARIOS WHERE username='"+usuario.username+"' AND evento='"+usuario.evento+"'")

                interaccionesReales=[]
                usuarioActual=usuario.interaccionEvento

                for row in cursor2:
                    usuarioBusqueda=row[0]
                    usuarioBusqueda=((usuarioBusqueda.replace("[","")).replace("]","")).split(")")
                    usuarioBusquedaTuplas=[(t.replace(", ","",1))+")" for t in usuarioBusqueda if usuarioBusqueda.index(t)!=0]
                    try:
                        usuarioBusquedaTuplas.remove(')')
                    except:
                        continue
                    usuarioBusquedaTuplas.insert(0, usuarioBusqueda[0]+")")
                    usuarioBusquedaTuplas=[make_tuple(i) for i in usuarioBusquedaTuplas]
                    ids=[id for num, id in usuarioBusquedaTuplas]
                    interaccionesReales=[(1,id) for _, id in usuarioActual if id not in ids]

                if not interaccionesReales:
                    conn.execute("INSERT INTO USUARIOS VALUES (?, ?, ?, ?,?,?,?, ?, ?)",(usuario.id, usuario.username, usuario.localizacion, usuario.bio,
                                                                            str(usuario.coordenadas), str(interaccionesReales), sum(i for i,_ in interaccionesReales), usuario.evento, usuario.busqueda, usuario.fecha_ultimo_tweet(), usuario.numero_seguidores(), usuario.numero_amigos(), usuario.numero_tweets()));

    conn.commit()


def extraeTodosDatos(evento):

    almacenaDatos(CONEXION, evento=True)

    cursor=CONEXION.execute("SELECT * FROM USUARIOS WHERE evento='"+evento+"'")
    datos=[";".join([row[1],row[2].replace("None",''), ((row[3].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "", row[4].replace("None",''), str(row[5]), str(row[6]), row[7], row[8], str(row[9]), str(row[10]), str(row[11]), str(row[12])]) for row in cursor]

    return datos


def extrae_seguidores(usuario):

    conn=crearBD()
    almacenaDatos(CONEXION, followers=True)

    cursor=conn.execute("SELECT * FROM FOLLOWERS WHERE seguidorde='"+usuario+"'")

    '''return [(row[0],
             row[1].replace("None", ''),
             ((row[2].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "",
             row[3],
             row[4],
             row[5],
             row[6],
             row[7],
             row[8],
             row[9]) for row in cursor]'''

    return [(row[0],
             row[1].replace("None", ''),
             ((row[2].replace("\n",'')).replace(";", ",")).replace("\r", "") if row[3]!="None" else "",
             row[3],
             str(row[4]),
             str(row[5]),
             str(row[6]),
             str(row[7])) for row in cursor]


def modifica_followers(conn):

    conn.execute('''CREATE TABLE IF NOT EXISTS FOLLOWERS_alt
                    (USERNAME CHAR(100) NOT NULL,
                    LOCALIZACION CHAR(100) NULL,
                    BIO VARCHAR(1000) NULL,
                    SEGUIDORDE CHAR(100),
                    FECHAULTIMOTWEET VARCHAR(100),
                    NUMEROSEGUIDORES INTEGER,
                    NUMEROAMIGOS INTEGER,
                    NUMEROTWEETS INTEGER,
                    PRIMARY  KEY (USERNAME, SEGUIDORDE));''')

    conn.execute("INSERT INTO FOLLOWERS_alt SELECT username, localizacion, bio, seguidorde, fecha_ult_tweet, num_seguidores, num_tweets, num_tweets_ultsem FROM FOLLOWERS;")
    conn.execute("DROP TABLE IF EXISTS FOLLOWERS")
    conn.execute("ALTER TABLE FOLLOWERS_ALT RENAME TO FOLLOWERS")

    conn.commit()

def modifica_eventos(conn):

    conn.execute("ALTER TABLE USUARIOS ADD COLUMN fechaultimotweet VARCHAR(100)")
    conn.execute("ALTER TABLE USUARIOS ADD COLUMN numeroseguidores INTEGER")
    conn.execute("ALTER TABLE USUARIOS ADD COLUMN numeroamigos INTEGER")
    conn.execute("ALTER TABLE USUARIOS ADD COLUMN numerotweets INTEGER")

    conn.commit()


def cerrarConexion():
    CONEXION.close()


CONEXION=crearBD()




