
MATRIX = []

M= 2 
N= 3 

for i in range(M):
    MATRIX.append([])
    for j in range(N):
        while True:
            try:
                r= int(input(f"Enter red value for pixel [{i}, {j}]: "))
                g= int(input(f"Enter green value for pixel [{i}, {j}]: "))
                b= int(input(f"Enter blue value for pixel [{i}, {j}]: "))
                
                if 0<= r<= 255 and 0<= g<= 255 and 0<=b<= 255:
                    MATRIX[i].append((r, g, b))
                    break
                else:
                    print("Nhap gia tri 0 den 255 thoi")
            except ValueError:
                print("Loi dau vao.")

#doi chuyen mau
for r in range(M):
    for c in range(N):
        if MATRIX[r][c]== (255, 0, 0):
            MATRIX[r][c]= (255, 255, 255)  #do => trang
        else:
            MATRIX[r][c]= (0, 0, 0)  #all con lai sang den

for row in MATRIX:
    print(row)
