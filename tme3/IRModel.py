import numpy as np
from collections import Counter
import porter as p

class IRModel():
    """
    Squelette de classe permettant d'utiliser un modèle de Recherche d'Information.
    """
    def __init__(self, weighter):
        """
        Permet d'initialiser en indiquant le systeme de pondération utilisé
        
        :param weighter: Instance d'une classe Weighter

        :type weighter: Weighter
        """
        self.weighter = weighter
    
    def getScores(self, query):
        """
        Permet de retourner le score de chaque document selon le modèle choisi.
        
        :param query: La requete à considérer

        :type query: string
        
        :return: Le score de chaque document
        :rtype: dict[int: number]
        """
        pass
    
    def getRanking(self, query):
        """
        Permet de retourner un classement de document par pertinence selon le modèle choisi.
        
        :param query: L'id du document à considérer

        :type query: string
        
        :return: liste des identifiants des documents du corpus triés par ordre décroissant de pertinence
        :rtype: list[int]
        """
        #On transforme le dictionnaire key:valeur en list de couple (key, valeur)
        #On trie ensuite selon la valeur par ordre décroissant
        return [k for k, v in sorted(query.items(), key=lambda item: item[1], reverse = True)]




class Vectoriel(IRModel):
    """
    Permet de représenter le modèle vectoriel en RI.
    """
    def __init__(self, weighter, normalized = True):
        """
        Permet d'initialisé en indiquant le mode de calcul utilisé entre le produit scalaire (normalized = False) et le cosinus (normalized = True)
        
        :param normalized: Booleen indiquant le mode de calcul à effectuer

        :type normalized: boolean
        """
        super().__init__(weighter)
        self.normalized = normalized
        
    def getScores(self, query):
        """
        CF class IRModel
        """
        if(self.normalized == True):#calcul du cosinus
            return self.getScoresNormalized(query)
        else:#calcul du produit scalaire
            return self.getScoresNotNormalized(query)
        
    def getScoresNormalized(self, query):
        """
        Permet de récupérer le score en utilisant le cosinus entre les représentations vectorielles
        
        param query: La requete à considérer

        :type query: string
        
        :return: Le score de chaque document
        :rtype: dict[int: number]
        """
        prodScalaires = self.getScoresNotNormalized(query)#Permet de récupérer les produits scalaires avec les différents documents
        res={}
        for docId,prod in prodScalaires.items():#Pour chaque produit scalaire, on divise par le produit des norm
            res[docId] = prod/(self.weighter.getNormDoc(docId)*self.weighter.getNormQuery(query))
        return res
    
    def getScoresNotNormalized(self, query):
        """
        Permet de récupérer le score en utilisant le produit scalaire entre les représentations vectorielles des documents
        
        param query: La requete à considérer

        :type query: string
        
        :return: Le score de chaque document
        :rtype: dict[int: number]
        """
        reqWeights = self.weighter.getWeightsForQuery(query) #On récupère les poids de la requetes
        res={}
        #Pour chaque terme de la requete (avec son poids associé)
        for stem,weightStem in reqWeights.items():
            docWeights = self.weighter.getWeightsForStem(stem)  #On récupère les poids du terme dans chaque document
            #Pour chaque document contenant le terme courant (et son poids associé)
            for docId,weightDoc in docWeights.items():
                if(docId not in res):#Si le document n'a pas encore été rencontré
                    res[docId] = weightStem*weightDoc#On ajoute le document avec comme valeur le produit des poids
                else:
                    res[docId] += weightStem*weightDoc#On ajoute le produit des poids à l'ancienne valeur
        return res    