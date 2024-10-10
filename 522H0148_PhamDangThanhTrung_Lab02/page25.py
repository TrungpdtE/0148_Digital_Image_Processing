# Khoi tao ma tran
MATRIX = []

# Lay kich thuoc tu nguoi dung
n=int(input("so hang= "))
m=int(input("so cot= "))

# Dien ma tran voi du lieu tu nguoi dung
for i in range(n):
    MATRIX.append([])
    for j in range(m):
        while True:
            inp= int(input("nhap gia tri (0-255) cho vi tri [{},{}]: ".format(i, j)))
            if 0<=inp<=255:
                MATRIX[i].append(inp)
                break
            else:
                print("lam on chi nhap tu 0-255")

# Chuyen doi
binary_matrix = []
for i in range(n):
    binary_row = []
    for j in range(m):
        if MATRIX[i][j]< 128:
            binary_row.append(0)  # den
        else:
            binary_row.append(255)  # trang
    binary_matrix.append(binary_row)

print("Ma tran goc:")
for row in MATRIX:
    print(row)

print("\nMa tran nhi phan:")
for row in binary_matrix:
    print(row)
