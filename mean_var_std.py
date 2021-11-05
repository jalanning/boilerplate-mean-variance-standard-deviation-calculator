import numpy as np

def calculate(list):

    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")
    
    a = np.array(list).reshape(3,3)

    def getVals(npfunc):
      return [npfunc(a, axis=0).tolist(), npfunc(a, axis=1).tolist(), npfunc(a)]

    calculations = {
      'mean': getVals(np.mean),
      'variance': getVals(np.var),
      'standard deviation': getVals(np.std),
      'max': getVals(np.max),
      'min': getVals(np.min),
      'sum': getVals(np.sum)
    }


    return calculations
