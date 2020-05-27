import random
import meta_bdd
from Student import *
from mode import Mode
from Meta_donnee import Meta_donnee
    
def subject():
    subjects = ['C', 'JAVA', 'Python']
    while(True):
        print("Listes des matières : ")
        for e in subjects:
            print("Entrez "+str(subjects.index(e))+" pour "+e)
        i = int(input("Votre choix : "))
        switcher={
            0:'C',
            1:'JAVA',
            2:'Python',
        }
        a = switcher.get(i,False)
        if(a == False):
            print("Matière invalide")
            continue
        else:
            return a

def notion(subject):
    notions = {
        'C': ['program', 'array', 'string', 'function','variable','type','input_output','pointer','allocation','macro','recursion','bitwise'], 
        'Python': ['program', 'array', 'string', 'function','variable','input_output'], 
        'JAVA': ['program', 'array', 'string', 'function','type','input_output']
    }
    while(True):
        print("Listes des notions : ")
        for e in notions[subject]:
            print("Entrez "+str(notions[subject].index(e))+" pour "+e)
        i = int(input("Votre choix : "))
        if(subject == "C"):
            switcher={
                0:notions[subject][0],
                1:notions[subject][1],
                2:notions[subject][2],
                3:notions[subject][3],
                4:notions[subject][4],
                5:notions[subject][5],
                6:notions[subject][6],
                7:notions[subject][7],
                8:notions[subject][8],
                9:notions[subject][9],
                10:notions[subject][10],
                11:notions[subject][11]
            }
        elif(subject == "JAVA"):   
            switcher={
                0:notions[subject][0],
                1:notions[subject][1],
                2:notions[subject][2],
                3:notions[subject][3],
                4:notions[subject][4],
                5:notions[subject][5]
            }
        elif(subject == "Python"): 
            switcher={
                0:notions[subject][0],
                1:notions[subject][1],
                2:notions[subject][2],
                3:notions[subject][3],
                4:notions[subject][4],
                5:notions[subject][5]
            }
        a = switcher.get(i,False)
        if(a == False):
            print("Notion invalide")
            continue
        else:
            print(a)
            return a

def next_exercice(meta,dico,student,mode,subject,tag):
    if (mode == Mode.decouverte):
        return meta.tag(tag,student,subject)
    elif (mode == Mode.revision):
        newTag = meta.newTagRev(student,subject,tag)
        return meta.tagRev(newTag,student)
    elif (mode == Mode.remise):
        newTag = meta.newTagRev(student,subject,tag)
        return meta.tagRemise(newTag,student) 

if __name__ == '__main__':
    meta = Meta_donnee(list())
    meta.initialise_meta()
    skills = list()
    skills.append({'C': { 'skills': {'program':8, 'function':8}}})
    skills.append({'C': { 'skills': {'string':1, 'array':1, 'program':4}}})
    skills.append({})
    skills.append({'C': { 'skills': {'string':10, 'array':10, 'program':0,'function':10,
    'variable':10, 'type':10,'pointer':0,'input_output':0,'allocation':0,'structure':10,'macro':0,'recursion':10,'bitwise':10}}})
    skills.append({'C': { 'skills': {'string':1, 'array':1, 'program':3,'function':1, 'variable':1}}})

    students = list()

    # Découverte
    # Prendre un étudiant déjà fort sur une ou plusieurs notions et générer le parcours pour apprendre le reste des notions.
    #students.append(Student("Parcours precis 1",100,100,0,skills[0],dict(),dict()))

    # Remise à niveau
    # Prendre un étudiant avec un passif vierge (zéro dans toutes les notions) et tentez de rusher une ou plusieurs notions spécifiques.
    #students.append(Student("Parcours precis 2",100,100,0,skills[2],dict(),dict()))

    # Découverte
    #students.append(Student("Parcours precis 3 - Eleve Mauvais",30,75,0,skills[2],dict(),dict()))
    #students.append(Student("Parcours precis 3 - Eleve Moyen",50,75,0,skills[2],dict(),dict()))
    #students.append(Student("Parcours precis 3 - Eleve Bon",90,100,0,skills[2],dict(),dict()))


    dico_meta = meta_bdd.meta

    for s in students:
        print("=====================================================================================")
        print("Session de : "+s.name)
        print(s.profil)
        mode = Mode[input('Choissisez un des modes disponibles : ')]
        subjectChoose = subject()
        if(mode != Mode.decouverte):
            tag = notion(subjectChoose)
        else:
            tag = meta.newTag(subjectChoose,s)
        nb_exo = 50
        while(nb_exo != 0):
            nb_exo-=1
            exo = next_exercice(meta,dico_meta,s,mode,subjectChoose,tag)
            if not exo:
                print("Aucun exercice trouvé pour votre profil")
                break
            mark = s.genMark()
            refus = s.refuse()
            if refus:
                print("refusé")
                continue
            s.updateProfil(subjectChoose,exo[0],mark,exo[1])
            print("Exercice "+str(50-nb_exo))
            print(exo[1])
            print("Note reçu : "+str(mark)+" | profil : ", s.profil)
            meta.updatetag(tag,mark,s,subjectChoose,mode)
