from Weighter import Weighter

class Weighter1(Weighter):
    """
    CF class Weighter
    """
    def getWeightsForDoc(self, idDoc):
        """
        CF class Weighter
        """
        return self.index[idDoc] #correspond aux tfs des termes du document
    
    def getWeightsForStem(self, stem):
        """
        CF class Weighter
        """
        return self.indexInverse[stem] if stem in self.indexInverse else {} #correspond aux tfs du terme pour chaque document
    
    def getWeightsForQuery(self, query):
        """
        CF class Weighter
        """
        #récupère chaque stem de la requete et lui attribut une valeur de 1 car np.unique est utilisé
        return dict(Counter(np.unique(list(map(p.stem, query.split())))))