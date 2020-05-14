from Query import Query
import re

class ParserQuery():
    
    def parseQRY(chemin):
        """ 
        Fonction permettant de parser les fichers QRY (requêtes avec leurs identifiants et leur texte)
        """
        file = open(chemin, 'r') 

        res = {}
        currentI = None
        currentBalise = None 
        currentQuery = None

        while True:
            #lis une seule ligne
            line = file.readline()

            #si ligne vide, fin du fichier
            if not line:
                break

            #récupère la ligne sous forme de mots
            words=line.split()

            #Si la ligne n'est pas vide
            if(len(words)>0):
                #Test si on est sur une balise et laquelle
                if(words[0]==".I"):

                    if(currentQuery != None):
                        #J'enregistre la requete courante avant d'en créer une autre
                        res[currentQuery.getIdentifiant()] = currentQuery 

                    del currentQuery
                    currentQuery = Query(words[1])# Création d'une requete avec son identifiant
                    currentI = words[1]
                    currentBalise = 'I' 

                elif(words[0]==".W"):
                    currentBalise='W' #J'indique que je suis danc une balise W
                elif(words[0][0]=='.'): 
                    currentBalise='unknown' #J'indique que je suis dans une balsie inconnue
                else: 
                    #On est dans le contenu d'une balise
                    if(currentBalise=='W'):
                        currentQuery.addTexte(line)#J'ajoute la ligne au texte de la requête

        #J'enregistre la requête courante avant de quitter
        res[currentQuery.getIdentifiant()] = currentQuery

        file.close()
        return res
    
    
    def parseREL(chemin, reqs):
        
        file = open(chemin, 'r') 
        
        while True:
            #lis une seule ligne
            line = file.readline()

            #si ligne vide, fin du fichier
            if not line:
                break
            words=line.split()
            
            if int(words[0][0]) == 0:
                docPertinent = int(re.split('^0*',words[1])[1])
                reqs[int(words[0][1])].addDocspertinents(docPertinent)
            else:
                docPertinent = int(re.split('^0*',words[1])[1])
                reqs[int(words[0])].addDocspertinents(docPertinent)
                     
        file.close()
        return reqs