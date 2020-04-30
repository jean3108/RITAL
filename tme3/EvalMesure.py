import numpy as np
from collections import Counter
import porter as p
import re
from Weighter import Weighter1
from IRModel import Vectoriel

class EvalMesure():
    
    def __init__(self):
        self.query = None
        
    def evalQuery(self,liste):
        pass
    
    #GETTERS
    def getQuery(self):
        return self.query
    
    #SETTERS
    def setQuery(self, query):
        self.query = query


class Precision(EvalMesure):
    
    def __init__(self,k):
        
        super().__init__()
        self.rang = k #rang de précision
        
    def evalQuery(self, scores):
        """ scores: liste() -> [idDoc] dépend du modèle de poids adopté
        (trié par score décroissant)"""
        res = 0
        for i in range(self.rang):
            if scores[i] in self.query.getDocspertinents():
                res+=1
        return res/self.rang

class Rappel(EvalMesure):
    
    def __init__(self,k):
        
        super().__init__()
        self.rang = k #rang de rappel
        
    def evalQuery(self, scores):
        """ scores: liste() -> [idDoc] dépend du modèle de poids adopté
        (trié par score décroissant)"""
        res = 0
        for i in range(self.rang):
            if scores[i] in self.query.getDocspertinents():
                res+=1
        return res/len(self.query.getDocspertinents())

class NGCD(EvalMesure):
    
    def __init__(self,k):
        
        super().__init__()
        self.rang = k #nombre de résultats à considérer
        
    def evalQuery(self, scores):
        """ scores: liste() -> [idDoc] dépend du modèle de poids adopté
        (trié par score décroissant)"""
        
        #relevance of returned docs above
        rel = [1 if d in self.query.getDocspertinents() else 0 for d in scores]
        
        #sorted relevance rank
        sorted_rel = np.sort(rel, axis=0)[::-1]
        metric = np.log([2+i for i in range(self.rang)])
        dcg = np.sum(rel[:self.rang]/metric)
        dcg_max = np.sum(sorted_rel[:self.rang]/metric)
        
        if not dcg_max:
            return 0
        else:
            return dcg/dcg_max


class AP(EvalMesure):
    """Avg precision"""
    
    def __init__(self,k):
        
        super().__init__()
        self.rang = k
        
    def evalQuery(self, scores):
        """ calcul de la preci moyenne"""
        return np.mean([self.preci(scores,k) for k in range(self.rang)])
     
    def preci(self, scores, k):
        """ scores: liste() -> [idDoc] dépend du modèle de poids adopté
        (trié par score décroissant)"""
        res = 0
        for i in range(k):
            if scores[i] in self.query.getDocspertinents():
                res+=1
        return res/k