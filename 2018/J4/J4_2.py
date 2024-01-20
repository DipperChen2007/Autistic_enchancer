def check_four_corners(matrix):
    n = len(matrix) - 1
    a = matrix[0][0]
    b = matrix[0][n]
    c = matrix[n][0]
    d = matrix[n][n]
    if a < b  and c < d and a< c and b<d:
        return True
    else:
        return False
    
def rotate(matrix):
    copy = [[0]* len(matrix) for i in range(len(matrix))]
    copy.append()
    n = len(matrix) - 1
    for r in range(n + 1):
        for c in range(n + 1):
            copy[r][c] = matrix[n - c][r]
    return copy
def Sunflowers(matrix):
    while check_four_corners(matrix) == False:
        matrix =  rotate(matrix)  
    for i in range(len(matrix)):
        matrix[i] = map(str,matrix[i])
    for i_2 in range(len(matrix)):
        print(" ".join(matrix[i_2]))
def Take_input():
    matrix = []
    n = int(input())
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    return matrix
matrix = Take_input()
Sunflowers(matrix)