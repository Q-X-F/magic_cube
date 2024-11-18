# the verified semiperfect magic cube of any odd order

cube = []

n = int(input("Enter the order of your magic cube: "))
M = n * (n ** 3 + 1) / 2

# cover with uniform cube of 1s

for i in range(n):
    cube.append([])
    for j in range(n):
        cube[i].append([])
        for k in range(n):
            cube[i][j].append(1)

# superposition of trivial cubes

for i in range(n):
    for j in range(n):
        for k in range(n):
            cube[i][j][k] += ((i + j + k + 1) % n) * (n ** 2)
            cube[i][j][k] += ((i + j - k) % n) * n
            cube[i][j][k] += (i - j + k) % n


for i in range(n):
    for j in range(n):
        for k in range(n):
            cube[i][j][k] = int(cube[i][j][k])


# answer
print("ANSWER: ")

for i in range(n):
    print("i = " + str(i))
    for j in range(n):
        print(cube[i][j])
    print("---------------------------")


'''
print("VERIFICATION OF SUMS: ")

# main verification 1
ver_k = True
print("sums of each pillar parallel to k")
for i in range(n):
    for j in range(n):
        sum = 0
        for k in range(n):
            sum += cube[i][j][k]
        if sum == M:
            print(sum)
        else:
            print("ERROR ERROR ERROR ERROR ERROR " + str(sum))
            ver_k = False

# main verification 2
ver_j = True
print("sums of each pillar parallel to j")
for i in range(n):
    for k in range(n):
        sum = 0
        for j in range(n):
            sum += cube[i][j][k]
        if sum == M:
            print(sum)
        else:
            print("ERROR ERROR ERROR ERROR ERROR " + str(sum))
            ver_j = False

# main verification 3
ver_i = True
print("sums of each pillar parallel to i")
for j in range(n):
    for k in range(n):
        sum = 0
        for i in range(n):
            sum += cube[i][j][k]
        if sum == M:
            print(sum)
        else:
            print("ERROR ERROR ERROR ERROR ERROR " + str(sum))
            ver_i = False


# main diagonal verifications
ver_main_diagonal = True

pp_diasum = 0
for d in range(n):
    pp_diasum += cube[d][d][d]
print("++ diagonal sum")
print(pp_diasum)
if pp_diasum != M:
    ver_main_diagonal = False

pn_diasum = 0
for d in range(n):
    pn_diasum += cube[d][d][n - 1 - d]
print("+- diagonal sum")
print(pn_diasum)
if pn_diasum != M:
    ver_main_diagonal = False

np_diasum = 0
for d in range(n):
    np_diasum += cube[d][n - 1 - d][d]
print("-+ diagonal sum")
print(np_diasum)
if np_diasum != M:
    ver_main_diagonal = False

nn_diasum = 0
for d in range(n):
    nn_diasum += cube[d][n - 1 - d][n - 1 - d]
print("-- diagonal sum")
print(nn_diasum)
if nn_diasum != M:
    ver_main_diagonal = False


print("VERIFICATION OF NON-REPETITION: ")
thisset = set()
for i in range(n):
    for j in range(n):
        for k in range(n):
            thisset.add(cube[i][j][k])
print(len(thisset))
print(thisset)

print("Final verifications below:")
print("ver_k = " + str(ver_k))
print("ver_j = " + str(ver_j))
print("ver_i = " + str(ver_i))
print("ver_main_diagonal = " + str(ver_main_diagonal))

'''
