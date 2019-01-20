sol = 0
for i in range(999,99,-1):
    # print("i = {0}".format(i))
    for j in range(999,99,-1):
        if str(i*j) == str(i*j)[::-1]:
            # print(i*j)
            if i*j > sol:
                sol = i*j
print(sol)