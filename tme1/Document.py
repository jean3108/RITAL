class Document():
    
    def __init__(self, identifiant):
        self.identifiant=int(identifiant)
        self.titre=""
        self.date=None
        self.auteurs=[]
        self.expressions=[]
        self.texte=""
        self.liens=[]
    
    ###########
    # GETTERS #
    ###########
    
    def getIdentifiant(self):
        return self.identifiant
    
    def getTitre(self):
        return self.titre
        
    def getDate(self):
        return self.date
        
    def getAuteurs(self):
        return self.auteurs
    
    def getExpressions(self):
        return self.expressions
        
    def getTexte(self):
        return self.texte
        
    def getLiens(self):
        return self.liens
    
    ###########
    # SETTERS #
    ###########
    
    def setTitre(self, titre):
        self.titre=titre
        
    def setDate(self, date):
        self.date=date
        
    def setAuteurs(self, auteurs):
        self.auteurs=auteurs
    
    def setExpressions(self, expressions):
        self.expressions=expressions
        
    def setTexte(self, texte):
        self.texte=texte
        
    def setLiens(self, liens):
        self.liens=liens
        
    ############
    # METHODES #
    ############
    
    def addTitre(self, texte):
        self.titre+=texte
        
    def addAuteur(self, nom, prenom):
        if(prenom==''):
            self.auteurs.append([nom])
        else:
            self.auteurs.append([nom, prenom])
        
    def addExpression(self, expression):
        self.expressions.append(expression)
        
    def addTexte(self, texte):
        self.texte+=texte
        
    def addLien(self, lien):
        self.liens.append(lien)
     
    
    def __repr__(self): #TO FINISH
        
        #formater l'identifiant
        identifiant = "\n##########\nIDENTIFIANT : "+str(self.identifiant)+"\n"
        
        #Formater le titre
        titre = ""
        if(self.titre != ""):
            titre = "\nTITRE : \n"+str(self.titre)+"\n"
        
        #Formater la date
        date = ""
        if(self.date != None):
            date = "\nDATE : "+str(self.date)+"\n"
        
        #Formater les auteurs
        auteurs=""
        if(len(self.auteurs)>0):
            if(len(self.auteurs)==1):
                auteurs = "\nAUTEUR : \n"
            else:
                auteurs = "\nAUTEURS : \n"
                
            for auteur in self.auteurs:
                if(len(auteur)==2): #Si auteur sous la forme [nom, prenom]
                    auteurs+=auteur[0]+", "+auteur[1]+"\n"
                else: #Si auteur sous la forme [nom]
                    auteurs+=auteur[0]+"\n"
        
        #Formater les mots-clé
        expressions=""
        if(self.expressions != ['']):
            expressions = "\nMOTS-CLES : \n"
            for expression in self.expressions:
                expressions += expression+", "
            expressions = expressions[:-2]+'\n' #On enlève le "," du dernier mot-clé
        
        #Formater le texte
        texte=""
        if(self.texte != ''):
            texte = "\nTEXTE (extrait) : \n "
            texte += self.texte[:50]+"...\n" #N'affiche que les 50 premiers caractères
        
        #Formater les liens
        liens=""
        if(len(self.liens)>0):
            liens = "\nNOMBRE DE LIENS : "+str(len(self.liens))+"\n##########\n"
            
        return identifiant+titre+date+auteurs+expressions+texte+liens
    
        
    