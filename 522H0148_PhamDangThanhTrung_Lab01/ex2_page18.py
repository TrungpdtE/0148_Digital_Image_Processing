n=int(input("row= "))
m=int(input("col="))

if n<=4 or m<=4:
    print("Kich thuoc ma tran qua nho de tao vien day 2 pixels")
else:
    def fill_border(matrix):
        n=len(matrix)
        m=len(matrix[0])
        
        for r in range(n):
            for c in range(m):
                if r<2 or r>=n-2 or c<2 or c>=m-2:
                    matrix[r][c]=0 
                else:
                    matrix[r][c]=255
        return matrix

    # khoi tao ma tran voi gia tri 255
    matrix=[[255 for _ in range(m)] for _ in range(n)]

    # dien gia tri 0 cho cac vi tri tren bien cua ma tran
    filled_matrix=fill_border(matrix)

    # in ma tran
    for row in filled_matrix:
        print(row)