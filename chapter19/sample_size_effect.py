from matplotlib import pyplot as plt
import numpy as np
from scipy import stats


def sample_size_effect(
    max_sample_size: int = 3000,
    n_trials: int = 1000, 
    sd: float = 5, 
    mu_control: float = 100, 
    mu_treatment: float = 100.5
    ):
    sample_sizes = range(100, max_sample_size, 100)
    avgPvalues = []
    for s in sample_sizes:
        pValuesPerSampleSize = []
        for _ in range(n_trials):
            control = np.random.normal(loc=mu_control, scale=sd, size=s)
            tratement = np.random.normal(loc=mu_treatment, scale=sd, size=s)

            twoSampleTest = stats.ttest_ind(control, tratement, equal_var = True)
            pValue = twoSampleTest[1]
            pValuesPerSampleSize.append(pValue)
        avgPvalues.append(np.sum(pValuesPerSampleSize) / len(pValuesPerSampleSize))
    return sample_sizes, avgPvalues


def test_sample_size_effect():  
    maxN = 3000
    nTrialsPerSamplesize = 1000
    sd = 5
    meanControl = 100 
    meanTreatment = 100.5
    
    number_of_samples,  avgPvalues = sample_size_effect(
        max_sample_size=maxN,
        n_trials=nTrialsPerSamplesize,
        sd=sd,
        mu_control=meanControl,
        mu_treatment=meanTreatment
        )
    
    print(avgPvalues[:5])
    
    plt.plot(number_of_samples, avgPvalues, label="Mean p-value")
    plt.yscale("log")
    plt.xlabel("Sample size")
    plt.ylabel("p-value")
    plt.axhline(y=0.01, linestyle='dotted', color='r', label="p=0.01")
    plt.axhline(y=0.05, linestyle='dashed', color='r', label="p=0.05")
    plt.title(f"Gaussians with $\sigma={sd}$, $\mu_{1}={meanControl}$, $\mu_{2}={meanTreatment}$")
    plt.legend(loc="upper right")
    plt.show()
    

if __name__ == "__main__":
        
    print("*** Test sample size effect on p-value ***")
    test_sample_size_effect()