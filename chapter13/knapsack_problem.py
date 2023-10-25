import random
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from chapter12.greedy_algo import Item


def maxVal(toConsider, avail):
    """
    Args:
        toConsider (list): list of items
        avail (initeger or float): available weight

    Returns:
        tuple: Returns a tuple of the total value of a solution to the 0/1 knapsack problem and the items of that solution
    """

    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
        avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


def fastMaxVal(toConsider, avail, memo = {}):
    """  
    - We notice that available weight depends upon the total weight of the items taken, 
    but not on which items are taken or the total value of the items taken
    - We need to exploit the optimal substructure and overlapping subproblems to provide 
    a dynamic programming solution to the 0/1 knapsack problem. 
      - An extra parameter, memo, has been added to keep track of solutions to subproblems that have already been solved

    Args:
        toConsider (list): list of items
        avail (integer or float): available weight
        memo (dict, optional): lookup dictionary. Defaults to {}.

    Returns:
        tuple: the total value of a solution to the 0/1 knapsack problem and the items of that solution
    """
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
        fastMaxVal(toConsider[1:],
        avail - nextItem.getWeight(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
        avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
            
    memo[(len(toConsider), avail)] = result
    return result


def smallTest():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
        
    val, taken = maxVal(Items, 5)
    
    for item in taken:
        print(item)
        
    print('Total value of items taken =', val)
    
    
def buildManyItems(numItems, maxVal, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i), random.randint(1, maxVal), random.randint(1, maxWeight)))
    return items

def bigTest(numItems):
    items = buildManyItems(numItems, 10, 10)
    val, taken = maxVal(items, 40)
    print('Items Taken')
    for item in taken:
        print(item)
    print('Total value of items taken =', val)
    
    
if __name__ == "__main__":
    
    print("\nRunning smallTest")
    smallTest()
    
    print("---"*10)
    
    print("\nRunning bigTest")
    bigTest(numItems=10)
    
    print("\nRunning fastMaxVal")
    items = buildManyItems(numItems=100, maxVal=10, maxWeight=100)
    val, taken = fastMaxVal(items, 100)
    print("val: ", val)
    print("taken: ")
    for i in taken:
        print("  ", i)
