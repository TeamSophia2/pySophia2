from os import getenv
import pandas as pd
import mariadb
import sys



columns = ['id', 'country', 'media_outlet', 'url', 'title', 'text', 'date', 'year', 'journalist', 'month']
__username__ = ""#getenv('SOPHIA_USER')
__password__ = ""#getenv('SOPHIA_PASS')
__cursor__=None


############ 0 LOGGING #############
def set_credentials(username="sophia2api", password=""):
    """[summary]

    Args:
        username (str, optional): [description]. Defaults to "sophia2api".
        password (str, optional): [description]. Defaults to "".
    """
    global __username__, __password__
    __username__ = username
    __password__= password
    return connect_sun()

def connect_sun(host="45.79.130.8", port=14096, database="Sun"):
    """[summary]

    Args:
        host (str, optional): [description]. Defaults to "45.79.130.8".
        port (int, optional): [description]. Defaults to 14096.
        database (str, optional): [description]. Defaults to "Sun".

    Returns:
        [type]: [description]
    """
    global __cursor__
    try:
        conn = mariadb.connect(
            user=__username__,
            password=__password__,
            host=host,
            port=port,
            database=database
        )
        __cursor__ = conn.cursor()
        return "successful connection"
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return "connection could not be established"

def __connection_validator():
    if __cursor__ is None: sys.exit("connect to the database first with: db.set_credentials(password)")

############ 1 INFO #############

def list_countries():
    """provides a list with all the countries that currently have media outlets in Sun

    Returns:
        [string]: [country_name]
    """
    __connection_validator()
    __cursor__.execute("SELECT DISTINCT country FROM news")
    return [x[0] for x in __cursor__.fetchall()]

def list_media_outlets(countries=["all"]): 
    pd.set_option("display.max_rows",None)
    __connection_validator()
    if "all" in countries: countries=list_countries()
    media_outlets=[]
    for country in countries:
        __cursor__.execute("SELECT DISTINCT media_outlet FROM news WHERE country=?",(country,))
        for media_outlet in __cursor__.fetchall():
            media_outlets.append((country, media_outlet[0]))
    return pd.DataFrame(media_outlets,columns=["country", "media_outlet_name"])


def stats_countries():
    __connection_validator()
    __cursor__.execute("SELECT country, count(id) FROM news GROUP BY country")
    return pd.DataFrame(__cursor__.fetchall(),columns=["country", "quantity"])
    

def stats_countries_by_date(_from, _to):
    __connection_validator()
    __cursor__.execute("SELECT country, count(id) FROM news WHERE date >= ? AND date <= ? GROUP BY country",(_from,_to))
    return pd.DataFrame(__cursor__.fetchall(),columns=["country", "quantity"])
    

def stats_media_outlet():
    pd.set_option("display.max_rows",None)
    __connection_validator()
    __cursor__.execute("SELECT country, media_outlet, count(id) FROM news GROUP BY media_outlet")
    return pd.DataFrame(__cursor__.fetchall(),columns=["country", "media_outlet_name", "quantity"])

def stats_media_outlet_by_country(country='chile'):
    pd.set_option("display.max_rows",None)
    __connection_validator()
    __cursor__.execute("SELECT country, media_outlet, count(id) FROM news WHERE country = ? GROUP BY media_outlet",(country,))
    return pd.DataFrame(__cursor__.fetchall(),columns=["country", "media_outlet_name", "quantity"])

def stats_media_outlet_by_country_by_date(country='chile'): #por desarrollar
    __connection_validator()
    __cursor__.execute("SELECT country, media_outlet, count(id) FROM news WHERE country = ? GROUP BY media_outlet",(country,))
    return pd.DataFrame(__cursor__.fetchall(),columns=["country", "media_outlet_name", "quantity"])


############ 2 DATASETS #############

def last_n(n=1):
    __connection_validator()
    __cursor__.execute("SELECT *, month(date) as month FROM news ORDER BY ID DESC LIMIT ?" , (n,))
    return pd.DataFrame(__cursor__.fetchall(), columns=columns)

def dataset_by_country(country, _from, _to):
    __connection_validator()
    __cursor__.execute("SELECT *, month(date) as month FROM news WHERE date >= ? AND date <= ? AND country = ?", (_from, _to, country))
    return pd.DataFrame(__cursor__.fetchall(), columns=[columns])


def load_dataset():
		data = {'id':[1,2], 
'country':['chile','france'],
'media_outlet':['latercera','mediapart'], 'url':['www','www'], 
'title':['un titulo','un titre'], 
'text':['un texto','un texte'], 
'date':['2020-01-01','2020-01-02']}
		df = pd.DataFrame(data=data)
		return df

#save on js? as parameter of load or another function especially for download?
#if __username__ is None: set_credentials()