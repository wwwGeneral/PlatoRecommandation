from enum import Enum,auto

class Mode(Enum):
	decouverte= auto()
	revision = auto()
	remise = auto()
	def describe(self):
		 return self.name, self.value
	
	def getValue(self):
		return self.value
