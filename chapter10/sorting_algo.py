import time
import random
random.seed(123)


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time)
        print(f"Execution time: {elapsed_time_ms:.3f} nanoseconds")
        return result
    return wrapper



def selection_sort_v1(L):
    """
    Hypothesis: Assumes that L is a list of elements that can be compared using >.
    
    Return: L sorted in ascending order"""
    
    suffixStart = 0
    while suffixStart != len(L):
        #look at each element in suffix
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                #swap position of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1       
    return L

def selection_sort_v2(L):
    for i in range(len(L) - 1):
        min_index = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min_index]:
                min_index = j
        temp = L[i]
        L[i] = L[min_index]
        L[min_index] = temp   
    return L
        
 
def merge(left, right, compare):
    """
    Hypothesis: Assumes left and right are sorted lists and compare defines an ordering on the elements.
    
    Return: A new sorted (by compare) list containing the same elements as (left + right) would contain.
    """

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L, compare = lambda x, y: x < y):
    """
    Hypothesis: Assumes L is a list, compare defines an ordering on elements of L
    
    Return: A new sorted list with the same elements as L
    """
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)
 

if __name__ == "__main__":
    
    print('*** Test selection sort *** ')
    
    l = random.sample(range(1, 100), 13)
    
    functions_mappinp = {
        "selection_sort_v1": selection_sort_v1,
        "selection_sort_v2": selection_sort_v2,
        "merge_sort": merge_sort
    }
    
    for f in ["selection_sort_v1", "selection_sort_v2", "merge_sort"]:
        sorter = functions_mappinp[f]
        start_time = time.time_ns()
        res = sorter(l)
        print(f"res for {f}: ", res)
        end_time = time.time_ns()
        elapsed_time_ms = (end_time - start_time) / 1000
        print(f"=> Execution time for {f}: {elapsed_time_ms:.3f} milliseconds")
        
    

    
    
    

    
    