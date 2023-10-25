import time


def fib(n):
    """Assumes n is an int >= 0 Returns Fibonacci of n
    
    - The complexity of the implementation is a bit hard to derive, but it is roughly O(fib(n)). 
    That is, its growth is proportional to the growth in the value of the result, 
    and the growth rate of the Fibonacci sequence is substantial. 
    For example, fib(120) is 8,670,007,398,507,948,658,051,921. 
    If each recursive call took a nanosecond, fib(120) would take about 250,000 years to finish.
    
    - Remark: let's calculate fib(6)
    We notice that we are computing the same values over and over again. 
      - For example, fib gets called with 3 three times, and each of these calls provokes four additional calls of fib.
      - Optimization: record the value returned by the first call, and then look it up rather than compute it each time it is needed
    """
    
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

def fastFib(n, memo = {}):
    """
    Assumes n is an int >= 0, memo used only by recursive calls Returns Fibonacci of n
    
    Time complexity of fastFib(n) is O(n)
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
    

if __name__ == "__main__":
    
    
    for n in [10, 15, 20, 40]:
        print("\n" +  "-"*10)
        t0_start = time.time()
        print(f"fib({n}):  {fib(n)}")
        t0_end = time.time()
        t0 = t0_end - t0_start
        print(f"Runnng time for fib({n}):  {t0:.5f} seconds")
        
        t1_start = time.time()
        print(f"fastFib({n}): {fastFib(n)}")
        t1_end = time.time()
        t1 = t1_end - t1_start
        print(f"Runnng time for fastFib({n}): {t1:.5f} seconds")
        
        try:
            print(f"ration t0/t1:  => t0 = {(t0/t1):.5f} times t1,  when n = {n}")
        except ZeroDivisionError:
            print(f"diff t0 - t1 = {(t0 - t1):.5f} seconds,  when n = {n}")

            
        
    