from pandas import DataFrame
import pandas as pd
import pytest, os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#sys.path.append('../')
import sophia2

print(os.getcwd())

@pytest.fixture
def fixture_dataset():
	data = {'id':[1,2], 
'country':['chile','france'],
'media_outlet':['latercera','mediapart'], 'url':['www','www'], 
'title':['un titulo','un titre'], 
'text':['un texto','un texte'], 
'date':['2020-01-01','2020-01-02']}
	df = pd.DataFrame(data=data)
	return df

def test_load_dataset():

	dataset = sophia2.db.load_dataset()
	assert len(dataset) > 0
	assert type(dataset) is DataFrame


def test_get_nbdocuments(fixture_dataset):
	#print(fixture_dataset)
	nbdocuments=sophia2.sophia2.get_nbdocuments(fixture_dataset)
	assert nbdocuments == 2

#def test_connect_database():
#	user = "investigador"
#	password = "contraseña"
#	db = sophia2.__database()

