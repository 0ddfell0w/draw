import numpy as np
import scipy.stats

def ztop(z):
    '''
    Convert z-score to P-value for one sided hypothesis test
    '''
    return scipy.stats.norm.sf(abs(z))

def ztop2(z):
    '''
    Convert z-score to P-value for two sided hypothesis test
    '''
    return 2*scipy.stats.norm.sf(abs(z))
# def ptoz(p):

def zscore(x, mean, std):
    '''
    Return zscore for trial x given mean and standard deviation
    '''
    return (float(x) - mean) / std



