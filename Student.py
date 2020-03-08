from random import *
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
            if(not(self.profil.has_key(a[0]))):
                self.profil[a[0]] = a[1]*(mark/100)
            else:
                newMark = self.profil[a[0]]+(a[1]*(mark/100))/self.profil[a[0]]
                if(newMark <= 10):
                    self.profil[a[0]] = newMark
                else:
                    self.profil[a[0]] = 10

    def refuse(self):
        randomvalue = random()
        if (self.pRefus>randomvalue):
            return True
        return False

    def getMarkMin(self):
        return self.markMin

    def getMarkMax(self):
        return self.markMax

    def genMark(self):
        return randint(self.markMin,self.markMax)

if __name__ == '__main__':
    s = Student(90,100,0.4,{ 'program':1,})
    print(s.genMark())
    print(s.refuse())