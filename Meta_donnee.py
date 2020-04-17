import meta_bdd
from Exercice import *
from random import random,randint

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
			if exo.similarTag(tag) and exo.hasPrequesites(student) and exo.getPath() not in student.hist:
				return (exo.getTag(),exo.getPath())
	
	def updatetag(self,tag,mark):
		if mark >= 70:
			for matiere in tag.keys():
				tag[matiere]+=1
		elif mark < 50:
			for matiere in tag.keys():
				tag[matiere]-=1
		return tag
	
	def testTag(self,tag):
		for exo in self.liste:
			print(exo.similarTag(tag))

##############################################################################################################

	def tagRev(self,tag,student):
			for exo in self.liste:
				if exo.similarTag(tag) and exo.hasPreForRev(student) and exo.getPath() not in student.hist:
					return (exo.getTag(),exo.getPath())
