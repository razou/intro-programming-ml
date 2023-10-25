from greedy_algo import Item, buildItems
import itertools

def generate_combinations(input_list):
    all_combinations = []
    n = len(input_list)

    for r in range(n + 1):
        combinations_r = itertools.combinations(input_list, r)
        all_combinations.extend([list(combination) for combination in combinations_r])

    return all_combinations



def chooseBest(pset, maxWeight, getVal, getWeight):
    """ Brute-force optimal solution to the 0/1 knapsack problem
    
    The complexity of this implementation is O(n*2^n), where n is the length of items. 
    The function genPowerset returns a list of lists of Items. This list is of length 2^n, 
    and the longest list in it is of length n. Therefore the outer loop in chooseBest 
    will be executed O(2^n)) times, and the number of times the inner loop will be executed is bounded by n.
    """
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)

def testBest(maxWeight = 20):
    items = buildItems()
    pset = generate_combinations(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue,
    Item.getWeight)
    print('Total value of items taken is', val)
    for item in taken:
        print(item)

if __name__ == "__main__":
    
    """
    Notice that this solution is better than any of the solutions found by the greedy algorithms. 
    The essence of a greedy algorithm is making the best (as defined by some metric) 
    local choice at each step. It makes a choice that is locally optimal. 
    However, as this example illustrates, a series of locally optimal decisions does not 
    always lead to a solution that is globally optimal.
    """
    testBest()