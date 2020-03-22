import meta_bdd
from Exercice import *

class Meta_donnee:
	def __init__(self,liste):
		self.liste = liste
	
	def add(self,exercice):
		self.liste.append(exercice)
	
	def initialise_meta(self):
		dico_meta = meta_bdd.meta
		for dico in dico_meta.items():
			exercice = Exercice(dico[0],dico[1]['author'],dico[1]['title'],dico[1]['subject'],dico[1]['tag'],dico[1]['prerequisites'])
			self.add(exercice)
	
	def getMeta(self):
		return self.liste
	def tag(self,tag,student):
		for exo in self.liste:
			if tag == exo.getTag() and exo.hasPrequesites(student):
				return exo.getTag()