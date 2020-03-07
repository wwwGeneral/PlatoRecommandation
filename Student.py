class Student:
    """Classe définissant un étudiant"""
    def __init__(self, noteMin, noteMax, pRefus, profil):
        self.noteMin = noteMin
        self.noteMax = noteMax
        self.pRefus = pRefus
        self.profil = profil

    def updateProfil(self, competences, note):
        """Permet de mettre à jour le profil de l'étudiant avec ses nouvelles compétences"""
        for a in competences.items():
            if(not(profil.has_key(a[0]))):
                self.profil[a[0]] = a[1]*(note/100)
            else:
                newMark = self.profil[a[0]]+(a[1]*(note/100))/self.profil[a[0]]
                if(newMark <= 10):
                    self.profil[a[0]] = newMark
                else:
                    self.profil[a[0]] = 10

    def getPRefus():
        return self.pRefus

    def getNoteMin():
        return self.noteMin

    def getNoteMax():
        return self.noteMax
