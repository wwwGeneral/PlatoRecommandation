from Exercice import Exercice
from random import random,randint,shuffle
from mode import Mode
import math
import meta_bdd

class Meta_donnee:
    """Classe contenant les exercices de la méta donnée"""


    def __init__(self,liste):
        self.liste = liste
        self.notion = set()
    
    def add(self,exercice):
        self.liste.append(exercice)
        self.notion.update(exercice.tag)
    
    def initialise_meta(self):
        """Initialise les données"""
        dico_meta = meta_bdd.meta
        for dico in dico_meta.items():
            exercice = Exercice(dico[0],dico[1]['author'],dico[1]['title'],dico[1]['subject'],dico[1]['tag'],dico[1]['prerequisites'])
            self.add(exercice)
    
    def getMeta(self):
        return self.liste


    def tag(self,tag,student,subject):
        """Retourne un tuple tag, chemin de l'exercice si un tag est trouvé et None sinon
        liste_not est l'ensemble des notions parcourus"""

        liste_not = set()
        while(True):
            for exo in self.liste:
                #Si l'élève possède les prérequis, si l'exercice possède un tag similaire et si l'exercice n'est pas présent dans l'historique on renvoie un tuple (tag de l'exercice,chemin)
                if exo.similarTag(tag) and exo.hasPrequesites(student) and exo.path not in student.hist:
                    return (exo.getTag(),exo.getPath())
            tag = self.newTag(subject,student)
            student_tag = self.getAcquiredTag(student,subject)
            liste_not.update(student_tag)
            #On ajoute la notion dans l'ensemble des notions parcourus"
            liste_not.update(tag)
            #Si toutes les notions sont parcourus et si il n'y a eu plus de tag a proposé à l'élève on considère qu'il n'y a plus d'exercice adapté pour son profil
            if not tag or liste_not == self.notion:
                return
    

    def getAcquiredTag(self,student,subject):
        """Renvoie les notions acquises par l'élève
        Une notion est considéré comme acquis lorsque son niveau dans cette notion est >=6"""
        acquired = set()
        for noti in student.profil[subject]['skills']:
            if student.profil[subject]['skills'][noti] >=6:
                acquired.add(noti)
        return acquired

    def findNewTag(self,subject,student):
        """Renvoie une notion pas encore exploré par l'élève ou pas encore acquise
        Si aucune notion est trouvé, cela veut dire que soit toutes la fonction ne renvoie rien."""

        if not student.profil.get(subject):
            student.profil[subject] = {'skills':{}}
        #On initie une liste de notion qui sera toujours mélangé pour éviter de tomber sur des notions déjà parcourus.
        notions = list(self.notion)
        shuffle(notions)
        for noti in notions:
            if noti not in student.profil[subject]['skills'] or (noti in student.profil[subject]['skills'] and student.profil[subject]['skills'][noti]<6):
                return noti
        return None

    def newTag(self,subject,student):
        """Renvoie un nouveau tag qui n'est pas présent dans le profil de l'élève, ou un tag qui n'est pas assez développé
        Si tous les tags sont explorés, la fonction ne renvoie rien et affiche un message."""
        notion = self.findNewTag(subject,student)
        if not student.profil:
            return {'program':1}
        if not notion:
            print('Veuillez changer de mode, vous avez déjà acquis des compétences dans les différentes notions du ' + subject)
            return
        if notion in student.profil[subject]['skills']:
            return {notion:round(student.profil[subject]['skills'][notion])}
        return  {notion:1}
        
    
    def updatetag(self,tag,mark,student,subject,mode):
        """Mets à jour le tag de parcours 
        Le tag de parcours est utilisé pour recommandé des nouveaux exercices, il est généré par rapport au profil de l'élève et incrémente de 1 lorsqu'un exercice est réussie note>70 
        et décrémente de 1 si un exercice est raté"""
        #Etant donné que c'est une fonction utilisé pour le mode découverte, il fait rien si l'élève utilise un autre mode.
        if mode != Mode.decouverte:
            return tag
        if mark >= 70:
            for matiere in tag.keys():
                tag[matiere]+=1
                if tag[matiere] >= 6:
                    tag = self.newTag(subject,student)
        elif mark < 50:
            for matiere in tag.keys():
                tag[matiere]-=1
                if tag[matiere] >= 1:
                    tag[matiere] = 1
        return tag
        
    def tagRemise(self,tag,student):
        for exo in self.liste:
            if exo.similarTag(tag) and exo.hasPreForRem(student) and exo.getPath() not in student.hist:
                return (exo.getTag(),exo.getPath())

##############################################################################################################

    def tagRev(self,tag,student):
            for exo in self.liste:
                if exo.hasPreForRev(student) and exo.getPath() not in student.hist:
                    return (exo.getTag(),exo.getPath())

    def newTagRev(self,student,subject,tag):
        """
        Retourne un nouveau tag en fonction de l'évolution de l'élève
        """
        newTag = {tag : 0}
        if not student.profil.get(subject):
            student.profil[subject] = {'skills':{}}
        for k,v in student.profil[subject]['skills'].items():
            if (k == tag):
                newTag = {tag : round(v)}
        return newTag