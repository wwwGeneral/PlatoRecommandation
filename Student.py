from random import random,randint
class Student:
    """Classe définissant un étudiant"""

    def __init__(self, markMin, markMax, pRefus, profil):
        self.markMin = markMin
        self.markMax = markMax
        self.pRefus = pRefus
        self.profil = profil

    def updateProfil(self, skills, mark):
        """Permet de mettre à jour le profil de l'étudiant avec ses nouvelles compétences"""
        for a in skills.items():
            if(mark >= 70):
                if(not(self.profil.get((a[0])))):
                    self.profil[a[0]] = a[1]*(mark/100)
                else:
                    newMark = (a[1]*(mark/100) + self.profil[a[0]]*2)/3
                    if(newMark <= 10):
                        if(a[1] > self.profil[a[0]]):
                            self.profil[a[0]] = newMark
                        else:
                            self.profil[a[0]] = self.profil[a[0]]
                    else:
                        self.profil[a[0]] = 10
            elif(mark < 50):
                if(self.profil.get((a[0])) and a[1]<=self.profil[a[0]]):
                    self.profil[a[0]] = (self.profil[a[0]]*3 + a[1]*(mark/100))/4

    def refuse(self):
        randomvalue = random()
        if (self.pRefus>randomvalue):
            return True
        return False

    def genMark(self):
        return randint(self.markMin,self.markMax)