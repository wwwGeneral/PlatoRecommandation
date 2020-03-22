import random
import meta_bdd
from Student import *
from mode import Mode

def next_exercice(dico,student,mode):
	if (mode == Mode.decouverte):
		for key in dico_meta.keys():
			tag = dico_meta[key]['tag']
			for tag_value in tag.items():
				if (tag_value==('program',1)):
					return tag
	elif (mode == Mode.revision):
		pass
	elif (mode == Mode.remise):
		for a in student.profil.keys():
			skills = student.profil[key]['skills']
			for skill in skills.items():
				if (tag == skill[0]):
					for key in dico_meta.keys():
						tagExo = dico_meta[key]['tag']
						for tag_value in tag.items():
							if (tag == tag_value[0] and tag_value[1] == skill[1]):
								return 	key
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

	for s in students:
		mode = Mode[input('Choissisez un des modes disponibles : ')]
		subject = input('Choisissez une matière : ')
		if(mode != Mode.decouverte):
			tag = input('Choisissez une notion : ')
		nb_exo = 20
		while(nb_exo != 0):
			nb_exo-=1
			exo = next_exercice(dico_meta,s,Mode.decouverte)
			mark = s.genMark()
			refus = s.refuse()
			if refus:
				print("refusé")
				continue
			s.updateProfil(subject,exo,mark)
			print("Note reçu : "+str(mark)+" | profil : ", s.profil)
	
		
	
