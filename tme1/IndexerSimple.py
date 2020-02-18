import numpy as np
import TextRepresenter as tr
pt=tr.PorterStemmer()

class IndexerSimple():
    
    def __init__(self, collection):
        self.collection = collection
        self.index = None
        self.indexInverse = None
        self.indexInverseNormalized = None
        
    def indexation(self):
        if(self.index == None ):
            #Création index
            self.index = {}
            for key in self.collection:
                doc=self.collection[key]
                docTexte = doc.getTitre()+" "+doc.getTexte()+" "+" ".join(doc.getExpressions())
                self.index[key] = pt.getTextRepresentation(docTexte)
            #Création index inversé pas normalisé
            self.indexInverse = {}
            for numDoc, dico in self.index.items():
                for word, tf in dico.items():
                    if(word not in self.indexInverse):
                        self.indexInverse[word]= {}
                    self.indexInverse[word][numDoc] = tf
            #Index inversé normalisé
            self.indexInverseNormalized = {}
            for key in self.indexInverse:
                factor = 1.0/sum(self.indexInverse[key].values())
                self.indexInverseNormalized[key] = {}
                for k in self.indexInverse[key]:
                    self.indexInverseNormalized[key][k] = factor*self.indexInverse[key][k]
                    
    def getTfsForDoc(self, docId):
        return self.index[docId]
    
    def getTfIDFsForDoc(self, docId):
        res = {}
        doc = self.index[docId]
        N = len(self.index)
        for word in doc:
            tf = doc[word]
            idf = np.log( (1+N) / (1+len(self.indexInverse[word])) )
            res[word] = tf*idf
        return res
    
    def getTfsForStem(self, stemKey):
        return self.indexInverse[stemKey]
    
    def getTfIDFsForStem(self, stemKey):
        res = {}
        stem = self.indexInverse[stemKey]
        N = len(self.index)
        for doc in stem:
            tf = self.index[doc][stemKey]
            idf = np.log( (1+N) / (1+len(stem)) )
            res[doc] = tf*idf
        return res
    
    def getStrDoc(self, docId):
        return self.collection[docId].getTexte()