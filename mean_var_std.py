import numpy as np

def calculate(l):
    #Error handling
    if len(l) < 9:
        raise ValueError("List must contain nine numbers.")
    #dict for answers
    calculations = {}
    #get our array in here
    a = np.array(l)
    #reshape into 3x3
    m = a.reshape((3,3))
    #get means
    meanAxisZero = list(m.mean(axis=0))
    meanAxisOne = list(m.mean(axis=1))
    meanAxisFlat = a.mean(axis=0)
    calculations['mean'] = [meanAxisZero,meanAxisOne,meanAxisFlat]
    #get variance
    varAxisZero = list(m.var(axis=0))
    varAxisOne = list(m.var(axis=1))
    varAxisFlat = a.var(axis=0)
    calculations['variance'] = [varAxisZero,varAxisOne,varAxisFlat]
    #get std dev
    stdAxisZero = list(m.std(axis=0))
    stdAxisOne = list(m.std(axis=1))
    stdAxisFlat = a.std(axis=0)
    calculations['standard deviation'] = [stdAxisZero,stdAxisOne,stdAxisFlat]
    #get max
    maxAxisZero = list(m.max(axis=0))
    maxAxisOne = list(m.max(axis=1))
    maxAxisFlat = a.max(axis=0)
    calculations['max'] = [maxAxisZero,maxAxisOne,maxAxisFlat]
    #get min
    minAxisZero = list(m.min(axis=0))
    minAxisOne = list(m.min(axis=1))
    minAxisFlat = a.min(axis=0)
    calculations['min'] = [minAxisZero,minAxisOne,minAxisFlat]
    #get sum
    sumAxisZero = list(m.sum(axis=0))
    sumAxisOne = list(m.sum(axis=1))
    sumAxisFlat = a.sum(axis=0)
    calculations['sum'] = [sumAxisZero,sumAxisOne,sumAxisFlat]


    return calculations
