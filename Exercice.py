from Student import *
class Exercice:
	def __init__(self,path,author,title,subject,tag,prequesites):
		self.path = path
		self.author = author
		self.title = title
		self.subject = subject
		self.tag = tag
		self.prequesites = prequesites
	
	def getPath(self):
		return self.path
		
	def getAuthor(self):
		return self.author
		
	def getTag(self):
		return self.tag
		
	def getTitle(self):
		return self.title

	def getPrequesites(self):
		return self.prequesites
		
	def getSubject(self):
		return self.subject
	
	def hasPrequesites(self,student):
		profil = student.profil
		if not self.prequesites:
			return True
		if profil.get(self.subject):
			subj = profil[self.subject]['skills']
			for p in self.prequesites.items():
				if not subj.get(p[0]):
					return False
				if subj[p[0]]<p[1]:
					return False
		return False


	def __str__(self):
		return "Path = "+self.path+" Author = "+self.author+" Title = "+self.title
	
        
