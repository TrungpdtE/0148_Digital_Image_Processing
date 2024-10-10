
n=int(input("row= "))
m=int(input("col= "))

#khoi tao ma tran
matrix = [[] for _ in range(n)]

# nhap gia tri vao ma tran
for i in range(n):
    for j in range(m):
        while True:
            inp=int(input("nhap gia tri (0-255) cho vi tri [{},{}]: ".format(i, j)))
            if 0<=inp<=255:
                matrix[i].append(inp)
                break
            else:
                print("lam on chi nhap tu 0-255")

def invert_colors(matrix):
    M=len(matrix)
    N=len(matrix[0])
    
    for r in range(M):
        for c in range(N):
            matrix[r][c]=255-matrix[r][c]
    
    return matrix

# Chuyen mau cua ma tran
inverted_matrix=invert_colors(matrix)

# In ma tran
for row in inverted_matrix:
    print(row)