class Query():
    def __init__(self, idQuery):
        self.identifiant = int(idQuery)
        self.texte = ""
        self.docsPertinents = []
     
    #GETTERS
    def getIdentifiant(self):
        return self.identifiant
        
    def getTexte(self):
        return self.texte
        
    def getDocspertinents(self):
        return self.docsPertinents
    
    # SETTERS
    def setTexte(self, texte):
        self.texte = texte
        
    def setDocspertinents(self, docs):
        self.docsPertinents = docs
        
        
    # METHODES
    def addTexte(self, texte):
        self.texte += texte
        
    def addDocspertinents(self,doc):
        self.docsPertinents.append(doc)