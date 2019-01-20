def isPrime(n):
    for i in range(2, round(n**0.5)+1):
        if n % i == 0 or n <= 1:
            return False
    return True
star = []
i = 1
while len(star) != 10001:
    i+=1
    if isPrime(i):
        star.append(i)
print(star)
print(star[10000])
