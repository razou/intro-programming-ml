import random
from matplotlib import pyplot as plt
import numpy as np

def variance(X):
    """Assumes that X is a list of numbers. Returns the standard deviation of X"""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)

def stdDev(X):
    """Assumes that X is a list of numbers. Returns the standard deviation of X"""
    return variance(X)**0.5

def plotMeans(numDicePerTrial, numDiceThrown, numBins, legend,color, style):
    means = []
    numTrials = numDiceThrown//numDicePerTrial
    for i in range(numTrials):
        vals = 0
        for j in range(numDicePerTrial):
            vals += 5*random.random()
        means.append(vals/numDicePerTrial)
        
    plt.hist(means, numBins, color = color, label = legend, 
             weights = np.array(len(means)*[1])/len(means), hatch = style
             )
    
    return sum(means)/len(means), variance(means)



if __name__ == "__main__":
    
    mean, var = plotMeans(1, 100000, 11, '1 die', 'w', '*')
    print('Mean of rolling 1 dice =', round(mean,4), 'Variance =', round(var,4))
    
    mean, var = plotMeans(100, 100000, 11, 'Mean of 100 dice', 'w', '//')
    print('Mean of rolling 100 dice =', round(mean, 4), 'Variance =', round(var, 4))
    
    plt.title('Rolling Continuous Dice')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.legend()
    
    plt.show()
