from enum import Enum,auto

class Mode(Enum):
    decouverte = "decouverte"
    revision = "révision"
    remise = "remise"
    
    
    def describe(self):
         return self.name, self.value
    
    def getValue(self):
        return self.value
