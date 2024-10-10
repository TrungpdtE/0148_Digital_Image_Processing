
MATRIX = []
avgI = 0

#n is the number of row
#m is the number of colum

n=int(input("row= "))
m=int(input("col= "))

for i in range(n):
    MATRIX.append([])
    for j in range(m):
        while True:
            inp=int(input("nhap gia tri (0-255) cho vi tri [{},{}]: ".format(i,j)))
            if 0<=inp<=255:
                MATRIX[i].append(inp)
                break
            else:
                print("lam on chi nhap tu 0-255")

for r in range(n):
    for c in range(m):
        avgI+=MATRIX[r][c]

avgI/=(n * m)

print("avgI =",avgI)