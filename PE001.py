import time

def sumMultiplesOf3or5Under(N):
    sum = 0
    for n in range(0, N):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

N = int(input("Enter the value of N: "))

start_time = time.time()
sum = sumMultiplesOf3or5Under(N)
end_time = time.time()

print("The sum of all multiples of 3 or 5 below {N} is: {sum}".format(N = N, sum = sum))

duration = round(end_time-start_time, 2)
print("Took {duration} seconds to run.".format(duration = duration))