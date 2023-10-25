from typing import Optional
import numpy as np
import matplotlib.pyplot as plt


def student_law(df: int, n: int, num_bins = 1000, t_stat: Optional[float] = None):
    tDist = []
    for _ in range(n):
        tDist.append(np.random.standard_t(df))
        
    plt.hist(tDist, bins = num_bins, weights = np.array(len(tDist)*[1.0])/len(tDist))
    if t_stat and t_stat != np.nan:
        plt.axvline(t_stat, color = 'w', linewidth=8)
        plt.axvline(-t_stat, color = 'w', linewidth=8)
    plt.title(f'T-distribution with {df} Degrees of Freedom')
    plt.xlabel('T-statistic')
    plt.ylabel('Probability')
    plt.show()

def test_student_law(tStat = -2.13165598142, NumSamples = 1e5, degree_of_freedom = 180):
    student_law(df=degree_of_freedom, n=int(NumSamples), t_stat=tStat)



if __name__ == "__main__":
    test_student_law()
