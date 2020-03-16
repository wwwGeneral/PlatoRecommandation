from enum import Enum,auto

class Mode(Enum):
	decouverte= 1
	revision = 2
	remise = 3
	
	
	def describe(self):
		 return self.name, self.value
	
	def getValue(self):
		return self.value
