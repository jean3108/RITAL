import re
from Document import Document

class Parser():
    
    def parseCacmCisi(chemin):
        file = open(chemin, 'r') 

        res = {}
        currentI = None
        currentBalise = None 
        currentDoc = None
        allExpressions=""

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

                    if(currentDoc != None):
                        #Je mets les mots clef du document courant dans une bonne forme
                        currentDoc.setExpressions(list(map(str.strip, allExpressions.split(","))))
                        allExpressions=""
                        #J'enregistre le document courant avant d'en créer un autre
                        res[currentDoc.getIdentifiant()] = currentDoc 

                    del currentDoc
                    currentDoc = Document(words[1])# Création du document avec son identifiant
                    currentI = words[1]
                    currentBalise = 'I' 

                elif(words[0]==".T"):
                    currentBalise='T' #J'indique que je suis danc une balise T
                elif(words[0]==".B"):
                    currentBalise='B' #J'indique que je suis danc une balise B
                elif(words[0]==".A"):
                    currentBalise='A' #J'indique que je suis danc une balise A
                elif(words[0]==".K"):
                    currentBalise='K' #J'indique que je suis danc une balise K
                elif(words[0]==".W"):
                    currentBalise='W' #J'indique que je suis danc une balise W
                elif(words[0]==".X"):
                    currentBalise='X' #J'indique que je suis danc une balise X
                elif(words[0][0]=='.'): 
                    currentBalise='unknown' #J'indique que je suis dans une balsie inconnue
                else: 
                    #On est dans le contenu d'une balise
                    if(currentBalise=='T'):
                        currentDoc.addTitre(line)#J'ajoute la ligne au titre
                    elif(currentBalise=='B'):
                        #extraire la date de la ligne
                        regex = re.compile(r'(\d{4})')
                        date = regex.search(line)
                        if(date != None):
                            currentDoc.setDate(int(date.group(0)))
                    elif(currentBalise=='A'):
                        #extraire l'auteur de la ligne
                        regex = re.compile(r'([a-zA-Z \'.-]+)\s*,\s*([a-zA-Z \'.-]+)\s*\n')
                        auteur = regex.search(line)
                        if(auteur != None):
                            nom = auteur.group(1)
                            prenom = auteur.group(2)
                        else:
                            nom = line[:-1]#Si le format n'est pas nom, prenoms, on prend toute la ligne comme le nom (sans le retour à la ligne)
                            prenom = ""
                        currentDoc.addAuteur(nom, prenom)
                    elif(currentBalise=='K'):
                        allExpressions+=line[:-1]#J'ajoute à l'ensemble des mots-clefs la ligne courante sans le retour a la ligne
                    elif(currentBalise=='W'):
                        currentDoc.addTexte(line)#J'ajoute la ligne au texte
                    elif(currentBalise=='X'):
                        currentDoc.addLien(words[0])#J'ajoute le lien


        #Je mets les mots clef du document courant dans une bonne forme avant de quitte
        currentDoc.setExpressions(list(map(str.strip, allExpressions.split(","))))
        allExpressions=""
        #J'enregistre le document courant avant de quitter
        res[currentDoc.getIdentifiant()] = currentDoc

        file.close()

        return res
