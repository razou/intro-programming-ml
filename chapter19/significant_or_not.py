import random
from scipy import stats


def significant_or_not():
    """
    Lyndsay and John have wasted an inordinate amount of time over the last several
    years playing a game called Words with Friends. They have played each other
    1,273 times, and Lyndsay has won 666 of those games, prompting her to boast,
    “I’m way better at this game than you are.” John asserted that Lyndsay’s claim was
    nonsense, and that the difference in wins could be (and probably should be) attributed entirely to luck.
    
    This function will perform a two-tailed one-sample test.
    Setup
        - Treat each of the 1,273 games as an experiment returning 1 if Lyndsay was the victor and 0 if she was not.
        - Choose the null hypothesis that the mean value of those experiments is 0.5.
        - Perform a two-tailed one-sample test for that null hypothesis (i.e Ho, the Lyndsay success was due 
        to chance)
    """
    numGames = 1273
    lyndsayWins = 666
    outcomes = [1.0]*lyndsayWins + [0.0]*(numGames-lyndsayWins)
    print('The p-value from a one-sample test is', stats.ttest_1samp(outcomes, 0.5)[1])
    

def significant_or_not_monte_carlo():
    numGames = 1273
    lyndsayWins = 666
    numTrials = 10000
    atLeast = 0
    for trial in range(numTrials):
        LWins, JWins = 0, 0
        for game in range(numGames):
            if random.random() < 0.5:
                LWins += 1
            else:
                JWins += 1
        if LWins >= lyndsayWins or JWins >= lyndsayWins:
            atLeast += 1
    print('Probability of result at least this', 'extreme by accident =', atLeast/numTrials)
    
    
if __name__ == "__main__":
    print("*** Test significant or not ***")
    significant_or_not()
    significant_or_not_monte_carlo()