import meta_bdd
from Exercice import *

class Meta_donnee:
	def __init__(self):
		self.liste = list()
	
	def add(self,exercice):
		self.liste.append(exercice)
	
	def initialise_meta(self):
		dico_meta = meta_bdd.meta
		for dico in dico_meta.items():
			exercice = Exercice(dico[0],dico[1]['author'],dico[1]['title'],dico[1]['subject'],dico[1]['tag'],dico[1]['prerequisites'])
			self.add(exercice)
	
	
	
			
	
