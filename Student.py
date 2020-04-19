from random import random,randint
class Student:
    """Classe definissant un etudiant"""

    def __init__(self, name, markMin, markMax, pRefus, profil, hist, histAll):
        """
        name : nom de l'etudiant
        markMin : note minimal qu'il peux avoir ( de 0 à 100 avec markMin <= markMax )
        markMax : note maximal qu'il peux avoir ( de 0 à 100 avec markMin <= markMax )
        pRefus : probabilité de refus ( nombre entre 0 et 1 )
        profil : dictionnaire contenant les capacites de l'etudiant dans chaque matière pour chaque notion de la matiere
        hist : dictionnaire contenant les exercices réussi et leurs tags associes faisant office d'historique
        histAll : dictionnaire contenant tout les exercices et leurs tags associes faisant office d'historique
        """
        self.name = name
        self.markMin = markMin
        self.markMax = markMax
        self.pRefus = pRefus
        self.profil = profil
        self.hist = hist
        self.histAll = histAll

    def updateProfil(self, subject, skills, mark, name):
        """
        Permet de mettre à jour le profil de l'etudiant avec ses nouvelles competences
        subject : nom de la matière
        skills : ensemble des notions de l'exercice avec leur niveau de difficulte
        mark : note eu a l'exercice
        name : nom de l'exercice
        """
        for a in skills.items():
            # On considère la réussite à partir d'une note de 70/100
            if(mark >= 70):
                if(not(self.profil.get(subject))):
                    self.profil[subject] = {}
                    self.profil[subject]['skills'] = {}
                    self.profil[subject]['skills'][a[0]] = a[1]*(mark/100)
                elif(not(self.profil[subject]['skills'].get((a[0])))):
                    self.profil[subject]['skills'][a[0]] = a[1]*(mark/100)
                else:
                    # On fait la moyenne entre la note de l'exercice relative à la réussite et la note du profil pour une progression relativement rapide
                    newMark = (a[1]*(mark/100) + self.profil[subject]['skills'][a[0]])/2 
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
                # Si on réussi l'exercice on le retient dans l'historique avec ses tags
                self.hist[name] = skills
            # On considère l'échec à partir d'une note strictement inférieur à 50
            elif(mark < 50):
                if(self.profil.get((a[0])) and a[1]<=self.profil[subject]['skills'][a[0]]):
                    # On fait la moyenne entre la note du profil * 3 et la note de l'exercice relative à la réussite pour une régression plus lente que la progression
                    self.profil[subject]['skills'][a[0]] = (self.profil[subject]['skills'][a[0]]*3 + a[1]*(mark/100))/4
            self.histAll[name] = skills

    def refuse(self):
        """
        Renvoie True ou False selon la probabilité de refus de l'élève
        """
        randomvalue = random()
        if (self.pRefus>randomvalue):
            return True
        return False

    def genMark(self):
        """
        Renvoie un entier compris entre markMin et markMax
        """
        return randint(self.markMin,self.markMax)
