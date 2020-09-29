import time
import math

# returns true if m is divisible by 1,...,n
def isDivisible(m, n):
    for i in range(1, n+1):
        if m % i != 0:
            return False
    return True

def smallestMultiple(n):
    multiple = 1
    while True:
        if isDivisible(multiple, n):
            return multiple
        multiple += 1

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
    
def lcm(a, b):
    return a * (b // gcd(a, b))
    
def smallestMultipleEuclid(n):
    res = 1
    for i in range(2, n+1):
        res = lcm(res, i)
    return res

# computes all primes up to n
def sieveOfEratosthenes(n):
    isPrime = [True] * (n + 1)
    primes = []
    for i in range(2, len(isPrime)):
        if isPrime[i]:
            primes.append(i)
            for j in range(2*i, len(isPrime), i):
                isPrime[j] = False
    return primes

def smallestMultipleEratosthenes(n):
    res = 1
    primes = sieveOfEratosthenes(n)
    for p in primes:
        largestPower = math.floor(math.log(n, p))
        res *= p**largestPower
    return res

print("Select an algorithm (enter an integer from 1 to 2):")
print("(1) Naive - does trial division on each positive integer until the least common multiple of {1, ..., N} is found")
print("(2) Euclid - uses the Euclidean algorithm to compute the least common multiple of {1, ..., N}")
print("(3) Eratosthenes - uses a sieve to generate all primes p <= N, then finds the product over p of the largest p^k <= N.") 

alg = int(input())
N = int(input("Enter the value of N: "))

start_time = time.time()
if alg == 1:
    lcm = smallestMultiple(N)
elif alg == 2:
    lcm = smallestMultipleEuclid(N)
elif alg == 3:
    lcm = smallestMultipleEratosthenes(N)
end_time = time.time()

if alg == 1 or alg == 2 or alg == 3:
    print("The smallest positive number evenly divisible by all integers from 1 to {N} is: {lcm}".format(N = N, lcm = lcm))
    duration = round(end_time-start_time, 2)
    print("Took {duration} seconds to run.".format(duration = duration))
else:
    print("Invalid algorithm choice.")