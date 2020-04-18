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
                5:notions[subject][5],
                6:notions[subject][6]
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
        return meta.tagRev(tag,student)
    elif (mode == Mode.remise):
        return meta.tagRemise(tag,student) 
if __name__ == '__main__':
    meta = Meta_donnee(list())
    meta.initialise_meta()
    skills = list()
    skills.append({'C': { 'skills': {'program':1, 'function':1}}})
    skills.append({'C': { 'skills': {'string':1, 'array':1, 'program':4}}})
    skills.append({})
    skills.append({'C': { 'skills': {'string':1, 'array':1, 'program':1,'function':1, 'variable':1}}})

    students = list()
    #students.append(Student("Jean",30,75,0,skills[2],dict()))
    #students.append(Student("Pierre",50,100,1,skills[0],dict()))
    students.append(Student("Albert",50,100,0,skills[1],dict()))
    #students.append(Student("Marcel",80,100,0.3,skills[3],dict()))

    dico_meta = meta_bdd.meta

    for s in students:
        print("=====================================================================================")
        print("Session de : "+s.name)
        print(s.profil)
        mode = Mode[input('Choissisez un des modes disponibles : ')]
        subjectChoose = subject()
        if(mode != Mode.decouverte):
            m = notion(subjectChoose)
            tag = { m : 1}
            for k,v in s.profil[subjectChoose]['skills'].items():
                if (k == m):
                    tag = {m : v}
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
