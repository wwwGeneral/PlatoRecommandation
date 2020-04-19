from Student import *
class Exercice:
    """Classe représentant un exercice"""

    def __init__(self,path,author,title,subject,tag,prequesites):
        self.path = path
        self.author = author
        self.title = title
        self.subject = subject
        self.tag = tag
        self.prequesites = prequesites

    def getPath(self):
        return self.path
    
    def getAuthor(self):
        return self.author
    
    def getTag(self):
        return self.tag
    
    def getTitle(self):
        return self.title

    def getPrequesites(self):
        return self.prequesites
    
    def getSubject(self):
        return self.subject

    def similarTag(self,tags):
        """self.tag est le tag de l'exercice
        tag est le tag qui s'adapte par rapport au mode
        recherche dans le tag en paramètre, un tag similaire à celui-ci, renvoie False si le tag n'est pas présent dans l'exercice ou si la difficulté de l'exercice est trop éloigné au niveau de l'élève.
        renvoie True sinon.
        tag similaire : un tag similaire est un tag qui a une difficulté proche d'un autre tag tagdiff-1 < tagsimilairediff < tagdiff+1"""


        for tag in tags.items():
            if tag[0] not in self.tag or (tag[0] in self.tag and (tag[1]-self.tag[tag[0]]>1 or tag[1]-self.tag[tag[0]]<-1)):
                return False
        return True


    def hasPrequesites(self,student):
        """Renvoie True si l'élève a les prérequis et False sinon
        L'élève a les prérequis si:
            L'exercice ne possède pas de prérequis
            L'élève possède tous les tags dans le prérequis
            La difficulté des prérequis de l'exercice est inférieur au niveau de l'élève"""
        profil = student.profil
        if not self.prequesites:
           return True
        if profil.get(self.subject):
           subj = profil[self.subject]['skills']
           for p in self.prequesites.items():
              if not subj.get(p[0]):
                return False
              if subj[p[0]]<p[1]:
                return False
           return True
        return False
##############################################################################################################

    def hasPreForRev(self,student):
        profil = student.profil
        if not self.prequesites:
            return False
        if profil.get(self.subject):
            subj = profil[self.subject]['skills']
            for p in self.prequesites.items():
                if not subj.get(p[0]):
                    return False
                if (subj[p[0]]==p[1]) or (subj[p[0]]+1 == p[1]):
                    return True
        return False
        
    def hasPreForRem(self,student):
        profil = student.profil
        if not self.prequesites:
            return True
        if profil.get(self.subject):
            subj = profil[self.subject]['skills']
            for p in self.prequesites.items():
                if not subj.get(p[0]):
                    return False
                if subj[p[0]]==p[1] or subj[p[0]]-1 == p[1]:
                    return True
        return False
        
    def __str__(self):
        return "Path = "+self.path+" Author = "+self.author+" Title = "+self.title