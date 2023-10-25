class Item(object):
    
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    
    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight
    
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', ' + str(self.weight) + '>'
        return result
    
    def value(item):
        return item.getValue()
    
    def weightInverse(item):
        return 1.0 / item.getWeight()
    
    def density(item):
        return item.getValue() / item.getWeight()


def greedy(items, maxWeight, keyFunction):
    """
    Assumes Items a list, maxWeight >= 0, keyFunction maps elements of Items to numbers
    
    Complexity:
    The number of iterations of the for loop is bounded by len(itemsCopy), i.e., it is O(n) and 
    the worst-case time for Python’s built-in sorting function is roughly O(n*log(n)).
    Therefore the running time of greedy is O(n*log(n))
    """
    
    itemsCopy = sorted(items, key=keyFunction, reverse = True)
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)


def buildItems():
    names = ['clock','painting','radio','vase','book','computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction)
    print('Total value of items taken is', val)
    for item in taken:
        print(' ', item)
        
def testGreedys(maxWeight = 20):
    items = buildItems()
    
    print('=> Use greedy by value to fill knapsack of size', maxWeight)
    testGreedy(items=items, maxWeight=maxWeight, keyFunction=lambda x: x.value) # best means most valuable
    
    print('\n=> Use greedy by weight to fill knapsack of size', maxWeight)
    testGreedy(items=items, maxWeight=maxWeight, keyFunction=lambda x: x.weightInverse()) # best means lowest weight
    
    print('\n=> Use greedy by density to fill knapsack of size', maxWeight) # best means highest density
    testGreedy(items=items, maxWeight=maxWeight, keyFunction=lambda x: x.density())
    

if __name__ == "__main__":
    
    # items = buildItems()
    # testGreedy(items=items, maxWeight=20, keyFunction=lambda x: x.value)
    
    testGreedys()