def harvest_value(patch, start_row, start_col):
    rows, cols = len(patch), len(patch[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def is_valid_move(row, col):
        return 0 <= row < rows and 0 <= col < cols and not visited[row][col] and patch[row][col] != '*'
    
    def dfs(row, col):
        visited[row][col] = True
        value = 0    
        if patch[row][col] == 'S':
            value += 1
        elif patch[row][col] == 'M':
            value += 5
        elif patch[row][col] == 'L':
            value += 10
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(new_row, new_col):
                value += dfs(new_row, new_col)
        
        return value
    
    return dfs(start_row, start_col)

def Take_input():
    R = int(input())
    C = int(input())
    patch = [input() for _ in range(R)]
    start_row = int(input())
    start_col = int(input())
    return patch,start_row,start_col

patch,start_row,start_col = Take_input()
print(harvest_value( patch,start_row,start_col))    

