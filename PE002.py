import time
import math

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    
def fibMemoized(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    cur = 1
    prev = 0
    
    for i in range(1, n):
        temp = cur
        cur += prev
        prev = temp
    
    return cur
    
def fibBinet(n):
    goldenRatio = (1 + math.sqrt(5))/2
    return round(goldenRatio**n / math.sqrt(5))
    
def sumEvenFib(N):
    sum = 0
    n = 1
    F_n = fib(n)
    while (F_n <= N):
        if F_n % 2 == 0:
            sum += F_n
        n += 1
        F_n = fib(n)
    return sum
    
def sumEvenFibMemoized(N):
    sum = 0
    n = 1
    F_n = fibMemoized(n)
    while (F_n <= N):
        if F_n % 2 == 0:
            sum += F_n
        n += 1
        F_n = fibMemoized(n)
    return sum
    
def sumEvenFibBinet(N):
    sum = 0
    n = 1
    F_n = fibBinet(n)
    while (F_n <= N):
        if F_n % 2 == 0:
            sum += F_n
        n += 1
        F_n = fibBinet(n)
    return sum

N = int(input("Enter the value of N: "))
print("Select an algorithm (enter an integer from 1 to 3):")
print("(1) Naive - computes fib(n) naively using the recurence relation")
print("(2) Memoized - computes fib(n) efficiently by storing previously computed results")
print("(3) Binet - computes fib(n) efficiently using Binet's formula")
alg = int(input())

start_time = time.time()
if alg == 1:
    sum = sumEvenFib(N)
elif alg == 2:
    sum = sumEvenFibMemoized(N)
elif alg == 3:
    sum = sumEvenFibBinet(N)
end_time = time.time()

if alg == 1 or alg == 2 or alg == 3:
    print("The sum of all even Fibonacci numbers at most {N} is: {sum}".format(N = N, sum = sum))
    duration = round(end_time-start_time, 2)
    print("Took {duration} seconds to run.".format(duration = duration))
else:
    print("Invalid algorithm choice.")