import time
import math

def largestPrimeFactor(n):
    primeFactors = [] 
    for k in range(2, n + 1):
        if n % k == 0:
            primeFactors.append(k)
            while n % k == 0:
                n //= k
    return primeFactors[len(primeFactors)-1]
        
def largestPrimeFactorOptimized(n):
    primeFactors = []
    
    upperBound = math.floor(math.sqrt(n))
    
    if n % 2 == 0:
        primeFactors.append(2)
        while n % 2 == 0:
            n //= 2
        upperBound = math.floor(math.sqrt(n))
    
    for k in range(3, upperBound + 1, 2):
        if n % k == 0:
            primeFactors.append(k)
            while n % k == 0:
                n //= k
            upperBound = math.floor(math.sqrt(n))

    if len(primeFactors) > 0:
        return primeFactors[len(primeFactors)-1]
    else:
        return n

N = int(input("Enter the value of n: "))
print("Select an algorithm (enter an integer from 1 to 2):")
print("(1) Naive - computes largest prime factor using trial division without optimization")
print("(2) Optimized trial division - computes largest prime factor using trial division with some optimizations")
alg = int(input())

start_time = time.time()
if alg == 1:
    p = largestPrimeFactor(N)
elif alg == 2:
    p = largestPrimeFactorOptimized(N)
end_time = time.time()

if alg == 1 or alg == 2:
    print("The largest prime factor of {N} is: {p}".format(N = N, p = p))
    duration = round(end_time-start_time, 2)
    print("Took {duration} seconds to run.".format(duration = duration))
else:
    print("Invalid algorithm choice.")