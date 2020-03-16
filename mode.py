from enum import Enum,auto

class Mode(Enum):
	decouverte = "decouverte"
	revision = "révision"
	remise = "révision"
	
	
	def describe(self):
		 return self.name, self.value
	
	def getValue(self):
		return self.value
