import time
import math

def reverse(n):
    res = 0
    while n > 0:
        res *= 10
        res += n % 10
        n //= 10
    return res

def isPalindrome(n):
    return reverse(n) == n
    
def largestPalindrome():
    max = 0
    for n in range(100, 1000):
        for m in range(100, 1000):
            if m*n > max and isPalindrome(m*n):
                max = m*n
    return max

"""
Optimized based on three observations:
1. mn has six digits since 110011 = 803 * 137.
   (This implies either m or n is divisible by 11)
2. We only need to search for n between max // m + 1 to 999
3. We can reduce the search space by searching from high to lower
   instead of low to high
"""
def largestPalindromeOptimized():
    max = 110011
    
    for m in range(990, 100, -11):
        lowerBound = max // m
        for n in range(999, lowerBound, -1):
            if isPalindrome(m*n):
                max = m*n
                break
    return max

print("Select an algorithm (enter an integer from 1 to 2):")
print("(1) Brute force - tries every combination of two 3-digit numberscomputes largest prime factor using trial division without optimization")
print("(2) Optimized - uses a reduced search space based on a few key observations")
alg = int(input())

start_time = time.time()
if alg == 1:
    P = largestPalindrome()
elif alg == 2:
    P = largestPalindromeOptimized()
end_time = time.time()

if alg == 1 or alg == 2:
    print("The palindromic number made from a product of two 3-digit numbers is: {P}".format(P = P))
    duration = round(end_time-start_time, 2)
    print("Took {duration} seconds to run.".format(duration = duration))
else:
    print("Invalid algorithm choice.")