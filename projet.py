import random
import meta_bdd

def next_exercice(dico,student,mode):
	
	pass
	#Gros algorithme permettant de recommander un exercice 
def generation():
	return random.randint(0,100)
	#TODO generer une note aléatoire à l'élève par rapport à son profil
	
def update_competence():
	pass

def refuser(prob):
	randomvalue = random.random()
	if (prob>randomvalue):
		return True
	return False
	
def update_comptence():
	pass
	#TODO update la compétence de l'élève
	
if __name__ == '__main__':
	
	dico_meta = meta_bdd.meta
	for dico_element in dico_meta.items():
		print(dico_element)
	while(True):
		next_exercice()
		mark = generation()
		refus = refuser(0.2)
		if refus:
			print("refusé")
			break
		update_competence()
	
		
	
