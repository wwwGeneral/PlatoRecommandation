class Exercice:
	def __init__(self,path,author,title,subject,tag,prequesites):
		self.path = path
		self.author = author
		self.title = title
		self.subject = subject
		self.tag = tag
		self.prequesites = prequesites
	
	def getPath():
		return self.path
		
	def getAuthor():
		return self.author
		
	def getTag():
		return self.tag
		
	def getTitle():
		return self.title

	def getPrequesites():
		return self.prequesites
		
	def getSubject():
		return self.subject
		
		
	def __str__(self):
		return "Path = "+self.path+" Author = "+self.author+" Title = "+self.title
	
        
