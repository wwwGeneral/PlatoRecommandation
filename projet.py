import random
import meta_bdd
from Student import *
from mode import Mode
    
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
        'C': ['program', 'array', 'string', 'function','variable','type','input_output','pointer'], 
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
                0:'program',
                1:'array',
                2:'string',
                3:'function',
                4:'variable',
                5:'type',
                6:'input_output',
                7:'pointer'
            }
        elif(subject == "JAVA"):   
            switcher={
                0:'program',
                1:'array',
                2:'string',
                3:'function',
                4:'variable',
                5:'type',
                6:'input_output'
            }
        elif(subject == "Python"): 
            switcher={
                0:'program',
                1:'array',
                2:'string',
                3:'function',
                4:'variable',
                5:'input_output'
            }
        a = switcher.get(i,False)
        if(a == False):
            print("Notion invalide")
            continue
        else:
            return a
def next_exercice(dico,student,mode,subject,tag):
    if (mode == Mode.decouverte):
        for key in dico_meta.keys():
            tag = dico_meta[key]['tag']
            for tag_value in tag.items():
                if (tag_value==('program',1)):
                    return tag
    elif (mode == Mode.revision):
        for key in dico_meta.keys():
            if (dico_meta[key]['subject'] == subject):
                tag = dico_meta[key]['tag']
                for k,v in dico_meta[key]['tag'].items():
                    for key,value in student.profil.items() :
                        if ((k == key) & (v == value)):
                            return tag

    elif (mode == Mode.remise):
        #Récupère le tag rentré, récupère le niveau de l'élève dans ce tag, puis cherche dans la bdd les exercices possédant ce tag et ce niveau de difficulté.
        matiere = s.profil.keys()
        for m in matiere:
            if (subject == m):
                for exercice in dico_meta.keys():
                    exoSubject = dico_meta[key]["subject"]
                    exoTag = dico_meta[key]["tag"]
                    exoPrerequisite = dico_meta[key]["prerequisites"]
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
                                    print("Il n'y a pas d'exercices correspondant au tag sélectionné")
                                    break
                        else:
                            print("Vous n'avez les prérequis")
                            break
                    else:
                        print("Il n'y a pas d'exercice dans cette matière")
                        break
            else:
                print("Vous n'avez pas la matière sélectionné dans votre profil")
                break    
    #Gros algorithme permettant de recommander un exercice 

if __name__ == '__main__':
    skills = list()
    skills.append({'C': { 'skills': {'program':1, 'function':1}}})
    skills.append({'C': { 'skills': {'string':1, 'array':1, 'program':4}}})
    skills.append({})
    skills.append({'C': { 'skills': {'string':1, 'array':1, 'program':1,'function':1, 'variable':1}}})

    students = list()
    students.append(Student("Jean",30,75,0,skills[2],[]))
    students.append(Student("Pierre",50,100,1,skills[0],[]))
    students.append(Student("Albert",50,100,0.5,skills[1],[]))
    students.append(Student("Marcel",80,100,0.3,skills[3],[]))

    dico_meta = meta_bdd.meta

    for s in students:
        tag =''
        print("=====================================================================================")
        print("Session de : "+s.name)
        mode = Mode[input('Choissisez un des modes disponibles : ')]
        subjectChoose = subject()
        if(mode != Mode.decouverte):
            tag = notion(subjectChoose)
        nb_exo = 20
        while(nb_exo != 0):
            nb_exo-=1
            exo = next_exercice(dico_meta,s,mode,subjectChoose,tag)
            mark = s.genMark()
            refus = s.refuse()
            if refus:
                print("refusé")
                continue
            s.updateProfil(subjectChoose,exo[0],mark,exo[1])
            print("Exercice "+str(20-nb_exo))
            print("Note reçu : "+str(mark)+" | profil : ", s.profil)
