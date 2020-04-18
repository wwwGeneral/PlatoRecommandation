from random import random,randint
class Student:
    """Classe définissant un étudiant"""

    def __init__(self, name, markMin, markMax, pRefus, profil, hist):
        """
        name : nom de l'étudiant
        markMin : note minimal qu'il peux avoir ( de 0 à 100 avec markMin <= markMax )
        markMax : note maximal qu'il peux avoir ( de 0 à 100 avec markMin <= markMax )
        pRefus : probabilité de refus ( nombre entre 0 et 1 )
        profil : dictionnaire contenant les capacités de l'étudiant dans chaque matière pour chaque notion de la matière
        hist : liste des noms des exercices réussi faisant office d'historique 
        """
        self.name = name
        self.markMin = markMin
        self.markMax = markMax
        self.pRefus = pRefus
        self.profil = profil
        self.hist = hist

    def updateProfil(self, subject, skills, mark, name):
        """Permet de mettre à jour le profil de l'étudiant avec ses nouvelles compétences
        subject : nom de la matière
        skills : ensemble des notions de l'exercice avec leur niveau de difficulté
        mark : note eu a l'exercice
        name : nom de l'exercice
        """
        for a in skills.items():
            if(mark >= 70):
                if(not(self.profil.get(subject))):
                    self.profil[subject] = {}
                    self.profil[subject]['skills'] = {}
                    self.profil[subject]['skills'][a[0]] = a[1]*(mark/100)
                elif(not(self.profil[subject]['skills'].get((a[0])))):
                    self.profil[subject]['skills'][a[0]] = a[1]*(mark/100)
                else:
                    newMark = (a[1]*(mark/100) + self.profil[subject]['skills'][a[0]]*2)/3
                    if(newMark <= 10):
                        if(a[1] > self.profil[subject]['skills'][a[0]]):
                            if(newMark > self.profil[subject]['skills'][a[0]]):
                                self.profil[subject]['skills'][a[0]] = newMark
                            else:
                                self.profil[subject]['skills'][a[0]] = self.profil[subject]['skills'][a[0]]
                        else:
                            self.profil[subject]['skills'][a[0]] = self.profil[subject]['skills'][a[0]]
                    else:
                        self.profil[subject]['skills'][a[0]] = 10
                self.hist[name] = skills
            elif(mark < 50):
                if(self.profil.get((a[0])) and a[1]<=self.profil[subject]['skills'][a[0]]):
                    self.profil[subject]['skills'][a[0]] = (self.profil[subject]['skills'][a[0]]*3 + a[1]*(mark/100))/4

    def refuse(self):
        randomvalue = random()
        if (self.pRefus>randomvalue):
            return True
        return False

    def genMark(self):
        return randint(self.markMin,self.markMax)
