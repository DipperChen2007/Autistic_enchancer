def H_W(patch,start_row,start_col):
    rows,cols = len(patch),len(patch[0])
    visited = [[False]*cols for _ in range(rows)]
    def if_move(row,col):
        return 0<=row<rows and 0<=col<cols and not visited[row][col] and patch[row][col] != "*"
    def dfs(row,col):
        visited[row][col] = True
        value = 0
        if patch[row][col] == "S":
            value += 1
        elif patch[row][col] == "M":
            value += 5
        elif patch[row][col] == "L":
            value += 10
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        for dr,dc in direction:
            new_row,new_col = row+dr,col+dc
            if if_move(new_row,new_col):
                value += dfs(new_row,new_col)
        return value
    return dfs(start_row,start_col)

def Take_input():
    r = int(input())
    c = int(input())
    patch = [input() for _ in range(c)]
    start_row = int(input())
    start_col = int(input())
    return patch,start_row,start_col

patch,start_row,start_col = Take_input()
print(H_W(patch,start_row,start_col))
