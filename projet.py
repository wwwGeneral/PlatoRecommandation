import random
import meta_bdd
from Student import *
from mode import Mode

def next_exercice(dico,student,mode,tag,subject):
	if (mode == Mode.decouverte):
		for key in dico_meta.keys():
			tage = dico_meta[key]['tag']
			for tag_value in tage.items():
				if (tag_value==("program",1)):
					return tage
	elif (mode == Mode.revision):
		pass
	elif (mode == Mode.remise):
		#Récupère le tag rentré, récupère le niveau de l'élève dans ce tag, puis cherche dans la bdd les exercices possédant ce tag et ce niveau de difficulté.
		matiere = s.profil.keys()
		for m in matiere:
			if (subject == m):
				for exercice in dico_meta.keys():
					exoSubject = dico_meta[key]["subject"]
					exoTag = dico_meta[key]["tag"]
					exoPrerequisite = dic_meta[key]["prerequisites"]
					if (exoSubject == subject):
						for prequisite in exoPrerequisite.items():
							for skill in s.profil[subject]["skills"]:
								if (skill[0] == prequisite[0] and skill[1] >= prequisite[1]):
									bon = True
								else:
									bon = False
						if (bon) :
							for t in exoTag.items():
								if (t[0] == tag):
									for skill in s.profil[subject]["skills"][tag]:
										if (skill[1] <= t[1]-1 and skill[1] > t[1] + 2):
											return exercice
										else:
											print("Votre niveau est trop élevé ou trop bas")
											break
								else:
									print("Il n'y a pas d'exercice correspondant au tag selectionner")
									break
						else:
							print("Vous n'avez les prérequis")
							break
					else:
						print("Il n'y a pas d'exercice dans cette matière")
						break
			else:
				print("Vous n'avez pas la matière séléctionné dans votre profil")
				break					
							



	
	#Gros algorithme permettant de recommander un exercice 

if __name__ == '__main__':
	skills = list()
	skills.append({'C': { 'skills': {'program':1, 'function':1}}})
	skills.append({'C': { 'skills': {'string':1, 'array':1, 'program':4}}})
	skills.append({})
	skills.append({'C': { 'skills': {'string':1, 'array':1, 'program':1,'function':1, 'variable':1}}})

	students = list()
	students.append(Student(30,75,0,skills[2]))
	students.append(Student(50,100,1,skills[0]))
	students.append(Student(50,100,0.5,skills[1]))
	students.append(Student(80,100,0.3,skills[3]))

	dico_meta = meta_bdd.meta
	test = True
	while test is True:
		for s in students:
			tag = ""
			mode = Mode[input('Choissisez un des modes disponibles : ')]
			subject = input('Choisissez une matière : ')
			if(mode != Mode.decouverte):
				tag = input('Choisissez une notion : ')
			nb_exo = 20
			while(nb_exo != 0):
				nb_exo-=1
				exo = next_exercice(dico_meta,s,mode,tag,subject)
				mark = s.genMark()
				refus = s.refuse()
				if refus:
					print("refusé")
					continue
				s.updateProfil(subject,exo,mark)
				print("Note reçu : "+str(mark)+" | profil : ", s.profil)
	
		
	
