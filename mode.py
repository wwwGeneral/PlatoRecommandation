from enum import Enum,auto
class Mode(Enum):
	decouverte= auto() # Exo de difficulté 1 voire 2 par compétences. Difficulté augmente un peu au fur et à mesure
	revision = auto() # Exo dont la difficulté des compétences est égale au niveau de l'élève sur ces compétences
	remise = auto() 
	
	 def describe(self):
		 return self.name, self.value
	
