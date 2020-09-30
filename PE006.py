import time

def sum(n):
    res = 0
    
    for i in range(1, n+1):
        res += i
    return res
    
def sumSquares(n):
    res = 0
    
    for i in range(1, n+1):
        res += i**2
    return res

def difference(n):
    return sum(n)**2 - sumSquares(n)

N = int(input("Enter the value of N: "))

start_time = time.time()
diff = difference(N)
end_time = time.time()

print("The difference between the sum of the squares of the first {N} positive integers and the square of the sum is is: {diff}".format(N = N, diff = diff))
duration = round(end_time-start_time, 2)
print("Took {duration} seconds to run.".format(duration = duration))