def successor(state):
    rtn = []
    new_state = state[:]
    for i in range(len(state)):
        current_top = state[i][0]
        left_top = state[i-1][0]
        right_top = state[i+1][0]
        if i == 0:
            if current_top > right_top:
                current_top = [right_top,current_top]
            
            

def dfs(start, goal):
    frontier = [(start, 0)]
    visited = set()

    while (frontier != []):
        current_state = frontier.pop()
        visited.add(current_state[0])

        if (current_state[0] == goal):
            return current_state[1]
        
        neighbours = successor(current_state)

        for neigh in neighbours:
            if (neigh not in visited):
                frontier.append((neigh, current_state[1]))
                
                
def Take_input():
    start = []
    n = int(input())
    for _ in range(n):
        start.append(list(map(int,input().split())))
    goal = sorted(start)
    return start,goal

# [[1],[2],[3],[2]]
# [[],[1,2],[3],[2]]


#[[[1],[2],[3],[2]],     [[],[1,2],[3],[2]],    [[],[1,2],[3],[2]]]