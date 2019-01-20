def div20(n):
    for i in range(20,1,-1):
        if n % i != 0:
            return False
    return True
found = False
i = 60
while not(found):
    i+=60
    found = div20(i)
print(i)