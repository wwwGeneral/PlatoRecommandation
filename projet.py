import random
import meta_bdd
from Student import *
from mode import Mode

def next_exercice(dico,student,goal,mode):
	if (mode == Mode.decouverte):
		for key in dico_meta.keys():
			tag = dico_meta[key]['tag']
			for tag_value in tag.items():
				if (tag_value==('program',1)):
					return tag
	elif (mode == Mode.revision):
		pass
	elif (mode == Mode.remise):
		pass
	
			
	pass
	#Gros algorithme permettant de recommander un exercice 

if __name__ == '__main__':
	goal = {'program':1}
	s = Student(50,100,0.1,dict())
	dico_meta = meta_bdd.meta
	for dico in dico_meta.values():
		print(dico)
	while(True):
		skills = next_exercice(dico_meta,s,goal,Mode.decouverte)
		mark = s.genMark()
		refus = s.refuse()
		if refus:
			print("refusé")
			break
		s.updateProfil(skills,mark)
	
		
	
