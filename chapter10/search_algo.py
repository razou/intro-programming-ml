import time


def linearSearch(L, e):
    """Assumes L is a list. Returns True if e is in L and False otherwise"""
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False


def binarySearch(L, e):
    """
    Assumes L is a list, the elements of which are in ascending order.
    
    Returns True if e is in L and False otherwise
    """
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e: 
            return False
    return False


def binarySearch_v2(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binarySearchWithRecursion(L, e):
    """   
    Assumes L is a list, the elements of which are in ascending order.
    
    Returns True if e is in L and False otherwise
    
    binarySearchWithRecursion is often called wrapper functions. it 
    provides a nice interface for client code, but is essentially a pass-through that 
    does no serious computation. Instead, it calls the helper function bSearch with 
    appropriate arguments. This raises the question of why not eliminate search and 
    have clients call bSearch directly? The reason is that the parameters low and high
    have nothing to do with the abstraction of searching a list for an element. They 
    are implementation details that should be hidden from those writing programs 
    that call search.
    """
 
    def bSearch(L, e, low, high):
        #Decrements high - low
        if high == low:
            return L[low] == e
        
        mid = (low + high)//2
        
        if L[mid] == e:
            return True
        
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)
        
    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)


if __name__ == "__main__":
    
    #random.sample(range(1,100), 30)
    lst = [91, 16, 63, 66, 7, 92, 23, 47, 29, 49, 3, 4, 6, 8, 26, 94, 69, 11, 80, 56, 55, 
           76, 64, 71, 17, 65, 46, 50, 9, 74]
    sorted_lst = sorted(lst, reverse=False)
    target = 3
    
    
    start = time.time()
    linearSearch(lst, target)
    end = time.time()
    print(f'Execution time for linear search: {end - start} seconds')

    
    start = time.time()
    binarySearch(sorted_lst, target)
    end = time.time()
    print(f'Execution time for binary search: {end - start} seconds')
    
    
    start = time.time()
    binarySearch_v2(sorted_lst, target)
    end = time.time()
    print(f'Execution time for binary search v2: {end - start} seconds')
    
    
    start = time.time()
    binarySearchWithRecursion(sorted_lst, target)
    end = time.time()
    print(f'Execution time for binary search with recursion: {end - start} seconds')