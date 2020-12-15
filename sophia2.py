import pandas as pd

class Sophia2:

	def __init__(self, user='guest', password='guest'):
		user=user
		password=password
		return ;

	def load_dataset(self):
		data = {'id':[1,2], 
'country':['chile','france'],
'media_outlet':['latercera','mediapart'], 'url':['www','www'], 
'title':['un titulo','un titre'], 
'text':['un texto','un texte'], 
'date':['2020-01-01','2020-01-02']}
		df = pd.DataFrame(data=data)
		return df

	def get_nbdocuments(dataset):
		return dataset.count()
