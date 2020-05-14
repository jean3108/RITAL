import numpy as np
from collections import Counter
import porter as p
import re
from Weighter import Weighter1
from IRModel import Vectoriel, Okapi
from EvalMesure import NGCD
from Parser import Parser
from ParserQuery import ParserQuery
from IndexerSimple import IndexerSimple

class EvalIRModel():
    
    def __init__(self, path):
        
        self.irModels = [] #(Liste)Objets IRModel (Vectoriel, Okapi, modèle de langue ...)
        self.evalMesures = [] #(Liste)Objets EvalMesure
        self.index = None #index des docs
        self.indexInverse = None #index inverse des docs
        self.querys = None #liste d'objets requêtes parsées (avec docs pertinents)
        self.path = path #cacm ou cisi
        
    def evaluationSimple(self,idIRModel, idEvalMesure):
        model, mesure = self.irModels[idIRModel], self.evalMesures[idEvalMesure]
        evals = []
        for idq,query in self.querys.items():
            mesure.setQuery(query)
            query_text = query.getTexte()
            scores = model.getScores(query_text)
            ranking = model.getRanking(scores)
            evals.append(mesure.evalQuery(ranking))
        return evals
    
    def evaluationQuery(self,idIRModel, idEvalMesure, idQuery):
        model, mesure, query = self.irModels[idIRModel], self.evalMesures[idEvalMesure], self.querys[idQuery]
        mesure.setQuery(query)
        query_text = query.getTexte()
        scores = model.getScores(query_text)
        ranking = model.getRanking(scores)
        evaluation = mesure.evalQuery(ranking)
        return evaluation
    
    def parseQuery(self):
        """Parse querys"""
        reqPath = self.path+'.qry'
        relPath = self.path+'.rel'
        r = ParserQuery.parseQRY('cacm.qry')
        querys = ParserQuery.parseREL('cacm.rel',r)
        self.querys = querys
        
    def parseDoc(self):
        """ Parse and index docs collection"""
        docsPath = self.path+'.txt'
        collecCacm = Parser.parseCacmCisi('cacm.txt')
        indexer=IndexerSimple(collecCacm)
        indexer.indexation()
        self.index, self.indexInverse = indexer.getIndex(), indexer.getIndexInv()
        
    def addModels(self, models):
        if type(models) == list:
            for m in models:
                self.irModels.append(m) 
        else:
            self.irModels.append(models)
            
    def addMesures(self, mesures):
        if type(mesures) == list:
            for m in mesures:
                self.evalMesures.append(m)
        else:
            self.evalMesures.append(mesures)
            
    def getQuerys(self):
        return self.querys
    
    def getIRModels(self):
        return self.irModels
    
    def getEvalMesures(self):
        return self.evalMesures
    
    def getIndex(self):
        return self.index
    
    def getIndexinverse(self):
        return self.indexInverse
    