import numpy as math


def concatPrimes(a, b, c, d, e):
    primes = [a, b, c, d, e]
    for i in primes:
        for j in primes:
            if i is j:
                continue
            elif not(isPrime(int(str(i) + str(j)))):
                return False
    return True


def isPrime(n):
    for i in range(2, int(math.round(math.sqrt(n)))):
        if n % i == 0 or n <= 1:
            return False
    return True


solution = [0, 0, 0, 0, 0]

keepGoing = True

i = 5
while keepGoing:
    i += 1
    if not(isPrime(i)):
        continue
    print(i)
    for j in range(0, i):
        if not(isPrime(j)):
            continue
        for k in range(0, j):
            if not(isPrime(k)):
                continue
            for l in range(0, k):
                if not(isPrime(l)):
                    continue
                for m in range(0, l):
                    if not(isPrime(m)):
                        continue
                    if concatPrimes(i,j,k,l,m):
                        keepGoing = False
                        solution = [i,j,k,l,m]
