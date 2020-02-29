class Weighter():
    """
    Classe abstraite représentant le squelette d'une pondération.
    """
    def __init__(self, index, indexInverse):
        """
        Permet d'initaliser en indiquant l'index et l'index inversé utilisé
        
        :param index: L'index considéré
        :param indexInverse: L'index inversé considéré

        :type index: dict[int : dict[string: int]]
        :type indexInverse: dict[string : dict[int: int]]
        """
        self.index = index
        self.indexInverse = indexInverse
        self.idf = {}
        self.norm = {}
        
    def getIdf(self, stem):
        """
        Permet de récupérer l'idf (index inverse frequency) d'une terme dans le corpus considéré.
        
        :param stem: Le terme dont l'idf doit être calculé

        :type stem: string
        
        :return: L'idf
        :rtype: float 
        """
        #Si l'idf du terme n'a jamais été calculé, on le calul et on l'enregistre avant de renvoyer la valeur
        if(stem not in self.idf):
            if(stem not in indexInverse):
                df = 0
            else:
                df = len(indexInverse[stem])
            self.idf[stem] = np.log((1+len(self.index)) / (1+df))
        return self.idf[stem]
    
    def getWeightsForDoc(self, idDoc):
        """
        Permet de récupérer les poids des termes du document indiqué.
        
        :param idDoc: L'id du document à considérer

        :type idDoc: int
        
        :return: Les poids des différents termes.
        :rtype: dict[string : number]
        """
        pass
    
    def getWeightsForStem(self, stem):
        """
        Permet de récupérer les poids du terme indiqué dans chaque document du corpus.
        
        :param stem: Le terme à considérer

        :type stem: string
        
        :return: Les poids du terme dans chaque document.
        :rtype: dict[int : number]
        """
        pass
    
    def getWeightsForQuery(self, query):
        """
        Permet de récupérer les poids de chaque terme dans la requete indiqué.
        
        :param query: La requete à considérer

        :type query: string
        
        :return: Les poids du terme dans la requete.
        :rtype: dict[string : number]
        """
        pass
    
    def getNormDoc(self, docId):
        """
        Permet de récupérer la norme d'un document vectorisé.
        
        :param docId: L'id du document à considérer

        :type docId: int
        
        :return: La norme du document vectorisé
        :rtype: float
        """
        #Si on n'a jamais calculé la norme du document, on le fait puis on l'enregistre avant de la retourner
        if(docId not in self.norm):
            docWeights = self.getWeightsForDoc(docId)#On récupère le poids de chaque terme du document dans un dictionnaire
            self.norm[docId] = np.linalg.norm(list(docWeights.values()))#On transforme en list/vecteur pour calculer la norme
            #Remarque : la norme d'un vecteur à N dimensions est égale à la norme de ce vecteur auquel on rajoute M dimensions nulles. (||[1,2]|| = ||[0,0,1,2]||)
        return self.norm[docId]
    
    def getNormQuery(self, query):
        """
        Permet de récupérer la norme d'une requete vectorisé.
        
        :param query: Requete à considérer

        :type query: string
        
        :return: La norme du document vectorisé
        :rtype: float
        """
        #On récupère le poids de chaque terme de la requete dans un dictionnaire
        reqWeights = self.getWeightsForQuery(query)
        #On transforme en list/vecteur pour calculer la norme
        #Remarque : la norme d'un vecteur à N dimensions est égale à la norme de ce vecteur auquel on rajoute M dimensions nulles. (||[1,2]|| = ||[0,0,1,2]||)
        return np.linalg.norm(list(reqWeights.values()))
    
    def getStemsFromQuery(query):
        """
        Permet de récupérer l'ensemble des termes d'une requete.
        
        :param query: Requete à considérer

        :type query: string
        
        :return: liste des termes de la requete
        :rtype: list[string]
        """
        return list(np.unique(list(map(p.stem, query.split())))) 
    
    