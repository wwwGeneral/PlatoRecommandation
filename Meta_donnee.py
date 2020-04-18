import meta_bdd
from Exercice import *
from random import random,randint,shuffle
from mode import Mode

class Meta_donnee:
    def __init__(self,liste):
        self.liste = liste
        self.notion = set()
    
    def add(self,exercice):
        self.liste.append(exercice)
        self.notion.update(exercice.tag)
    
    def initialise_meta(self):
        dico_meta = meta_bdd.meta
        for dico in dico_meta.items():
            exercice = Exercice(dico[0],dico[1]['author'],dico[1]['title'],dico[1]['subject'],dico[1]['tag'],dico[1]['prerequisites'])
            self.add(exercice)
    
    def getMeta(self):
        return self.liste


    def tag(self,tag,student,subject):
        while(True):
            for exo in self.liste:
                if exo.similarTag(tag) and exo.hasPrequesites(student) and exo.getPath() not in student.hist:
                    return (exo.getTag(),exo.getPath())
            tag = self.newTag(subject,student)
            print(tag)
            if not tag:
                return
    
    def findNewTag(self,subject,student):
        notions = list(self.notion)
        shuffle(notions)
        for noti in notions:
            if noti not in student.profil[subject]['skills']:
                return noti
        return None

    def newTag(self,subject,student):
        if not student.profil:
            return {'program':1}
        if not self.findNewTag(subject,student):
            print('Veuillez changer de mode, vous avez déjà acquis des compétences dans les différentes notions du ' + subject)
            return
        return  {self.findNewTag(subject,student):1}

    def updatetag(self,tag,mark,student,subject,mode):
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
            if exo.similarTagRemise(tag) and exo.hasPrequesites(student) and exo.getPath() not in student.hist:
                return (exo.getTag(),exo.getPath())
    
    

##############################################################################################################

    def tagRev(self,tag,student):
            for exo in self.liste:
                if exo.similarTag(tag) and exo.hasPreForRev(student) and exo.getPath() not in student.hist:
                    return (exo.getTag(),exo.getPath())
