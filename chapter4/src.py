import math

def isPositiveInteger(n):
    return isinstance(n, int) and n >= 0
    
def factI(n):
    """Compute fatcorial(n): iterative method
    
    Args:
        n (int): positive integer
    Returns:
        integer: n!
    """
    res = 1
    if isPositiveInteger(n):
        while n > 0:
            res = res * n
            n = n - 1
        return res
    else:
        raise ValueError("N should be positive int")


def factR(n: int) -> int:
    """Compute fatcorial(n): Recursive method

    Args:
        n (int): positive integer
    Returns:
        integer: n!
    """
    if isPositiveInteger(n):
        if n <= 1:
            return 1
        else:
            return n * factR(n - 1) 
 
def fibonacci(n: int) -> int:
    if isPositiveInteger(n):
        if n == 0 or n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)  
        

def isPalindrom(s: str)-> bool:
    """Using recursive function to check if a given string from a palindrom 

    Args:
        s (str):

    Returns:
        bool: True if alpahtic letters in s form a palindrom otherwise False
    """
    x = s.lower().strip()
    alpbetic_letters = [c for c in x if c.isalpha()]
    print("letters: ", alpbetic_letters)
    def is_palindrom(letters):
        if len(letters) <= 1:
            return True
        else:
            return letters[0] == letters[-1] and is_palindrom(letters[1:-1])
    return is_palindrom(alpbetic_letters)
    
    
              
if __name__ == "__main__":
    a = 8
    b = 14
    c = 5
    s1 = "ababa"
    s2 = "Ababa "
    s3 = "ababas"
    
    print("math.factorial(a): ", math.factorial(a))
    print("factI(a): ", factI(a))
    print("factR(a): ", factR(a))

    assert math.factorial(a) == factI(a)
    assert math.factorial(a) == factR(a)
    
    # print("-"*10)
    # # Fibonacci
    # for i in range(10):
    #     print(f"Fibonacci({i}) =  {fibonacci(i)}")
        
    print("-"*10)
    for s in [s1, s2, s3]:
        print(isPalindrom(s))
