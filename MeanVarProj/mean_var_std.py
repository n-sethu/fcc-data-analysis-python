import numpy as np

def calculate(input_list):
    if(len(input_list)!=9):
        raise ValueError("List must contain nine numbers.")
    mtrx=np.array(input_list).reshape(3, 3)
    calculations = {
        'mean': [list(mtrx.mean(axis=0)), list(mtrx.mean(axis=1)), float(np.mean(input_list))],
        'variance': [list(np.var(mtrx, axis=0)), list(np.var(mtrx, axis=1)), float(np.var(input_list))],
        'standard deviation': [list(np.std(mtrx, axis=0)), list(np.std(mtrx, axis=1)), float(np.std(input_list))],
        'max': [list(np.max(mtrx, axis=0)), list(np.max(mtrx, axis=1)), int(np.max(input_list))],
        'min': [list(np.min(mtrx, axis=0)), list(np.min(mtrx, axis=1)), int(np.min(input_list))],
        'sum': [list(np.sum(mtrx, axis=0)), list(np.sum(mtrx, axis=1)), int(np.sum(input_list))]
    }
    return calculations
calculate([2,6,2,8,4,0,1,5,7])