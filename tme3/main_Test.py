from Parser import Parser
from IndexerSimple import IndexerSimple
import numpy as np
from collections import Counter
import porter as p
import re
from Weighter import Weighter1
from IRModel import Vectoriel, Okapi
from EvalMesure import NGCD, Rappel, Precision
from EvalIRModel import EvalIRModel

PATH = 'cacm'

#Init evaluation
evalIRModel = EvalIRModel(PATH)

#Query/ Docs parsing (index creation)
evalIRModel.parseQuery()
evalIRModel.parseDoc()

#IRModels
#Index, IndexeInv
indexCacm, indexInvCacm = evalIRModel.getIndex(), evalIRModel.getIndexinverse()
weighter = Weighter1(indexCacm, indexInvCacm)
irModel1 = Vectoriel(weighter, True)
evalIRModel.addModels(irModel1)

# Eval Mesure
k=3 #rang
evalMesure1 = NGCD(k)
evalIRModel.addMesures(evalMesure1)

# Evaluation 
evalIRModel.evaluationSimple(0,0)

