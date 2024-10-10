n=int(input("row= "))
m=int(input("col= "))

def fill_middle(matrix):
    M=len(matrix)
    N=len(matrix[0])
    
    mid_row_start=(M-1)//2
    mid_row_end=M//2
    mid_col_start=(N-1)//2
    mid_col_end=N//2
    
    for r in range(mid_row_start,mid_row_end+1):
        for c in range(N):
            matrix[r][c]=255
    
    for c in range(mid_col_start,mid_col_end+1):
        for r in range(M):
            matrix[r][c] = 255
    
    return matrix

#khoi tao ma tran
matrix = [[0 for _ in range(m)] for _ in range(n)]

#dien gia tri vao ma tran
filled_matrix=fill_middle(matrix)

#in ma tran
for row in filled_matrix:
    print(row)