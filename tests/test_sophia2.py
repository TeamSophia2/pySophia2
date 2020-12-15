from sophia2 import Sophia2
from pandas import DataFrame
import pytest
import pandas as pd

def dataset():
	data = {'id':[1,2], 
'country':['chile','france'],
'media_outlet':['latercera','mediapart'], 'url':['www','www'], 
'title':['un titulo','un titre'], 
'text':['un texto','un texte'], 
'date':['2020-01-01','2020-01-02']}
	pd.DataFrame(data=data)
	return pd

def test_load_dataset():
	user = "investigador"
	password = "contraseña"
	sophia2 = Sophia2(user, password)
	dataset = sophia2.load_dataset()
	assert len(dataset) > 0
	assert type(dataset) is DataFrame

@pytest.fixture
def test_get_nbdocuments(dataset):
	sophia2 = Sophia2()
	nbdocuments=sophia.get_nbdocuments(dataset)
	assert nbdocuments is int
	assert nbdocuments == 2

#def test_connect_database():
#	user = "investigador"
#	password = "contraseña"
#	db = sophia2.__database()

