sol = 0
sol2 = 0
for i in range(1,101):
    sol+=i**2
    sol2+=i
print((sol2**2) - sol)