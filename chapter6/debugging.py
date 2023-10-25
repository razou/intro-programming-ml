def isPal(x: list) -> bool:
    """Assumes x is a list
    Returns True if the list is a palindrome; False otherwise
    """
    temp = x
    temp.reverse
    
    # for debug
    print("temp = ", temp, " and x = ", x)
    if temp == x:
        return True
    else:
        return False


def isPalTwo(x: list) -> bool:
    temp = x
    temp.reverse()
    
    print("temp = ", temp, " and x = ", x)
    if temp == x:
        print("temp = ", temp, " and x = ", x)
        return True
    else:
        return False
 
def isPalThree(x: list) -> bool:
    temp = x[:]
    temp.reverse()
    
    print("temp = ", temp, " and x = ", x)
    if temp == x:
        print("temp = ", temp, " and x = ", x)
        return True
    else:
        return False   
    
    
def silly_one(n: int) -> str:
    """Gets n inputs and print Yes if the sequence of inputs froms a palidrome;
    No otherwise.
    Assuming N is positive integer.

    Args:
        n (int): number of inputs
    """
    for i in range(n):
        result = []
        elem = input("Enter element: ")
        result.append(elem)
    # For debug
    # print("result: ", result)
    if isPal(result):
        print("Yes")
    else:
        print("No")
            
def silly_two(n: int) -> str:
    result = []
    for i in range(n):
        elem = input("Enter element: ")
        result.append(elem)
    print("result: ", result)
    if isPal(result):
        print("Yes")
    else:
        print("No")

def silly_three(n: int) -> str:
    result = []
    for i in range(n):
        elem = input("Enter element: ")
        result.append(elem)
    print("result: ", result)
    if isPalThree(result):
        print("Yes")
    else:
        print("No")
            
if __name__ == "__main__":
    
    import pandas as pd
    import numpy as np

    df = pd.DataFrame({
        "strings": ["Adam", "Mike"],
        "ints": [1, 3],
        "floats": [1.123, 1000.23]
    })

    df.style \
        .format(precision=3, thousands=".", decimal=",") \
        .format_index(str.upper, axis=1) \
        .relabel_index(["row 1", "row 2"], axis=0)
    raise
    
    
    # silly_one(2)
    
    """
    When testing silly_one() function always return yes (for every input)
    To debug it; we will find a halfway point and divide the experiment by two and 
    forgure out in which part the bugs may come from.
    Let's consider the line isPal() and print the value of the variable result
    We will notice that result is never more than on element (which is always a palindrom).
    Solution:  the initiliazation a the variable result needs to be move outside of the 
    for loop
    This is covert and persistent bug (the programm runs correctly but product wrong result)
    """
    
    silly_two(3)
    
    """
    Silly_two() still continue to print Yes.
    The content of the variable result is correct. 
    This suggets that a second bug lies below the print result statement.
    
    By looking ino the isPal function, the line if temp == x need to be checked. 
    Lets' insert print statement => temp and have same values
    
    The function reverse was not used corectly. 
        => temp.reverse => it returns the built-in reverse method for list but does not invoke it
        the correct usage is the following: temp.reverse()  (i.e parenthesis at the end )
    
    By fixing the usage of the revese method we found that the value of x is also reversed (isPalTwo)
        => this is an aliasing bug: temp and x are name for the same list
        To fix this make temp to be a copy of x, temp = x[:] (isPalThree))
    
    
    """
    
    # silly_three(3)