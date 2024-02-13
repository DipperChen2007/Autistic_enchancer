def successor(state):
    pass

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
                frontier.append((neigh, current_state[1] + 1))
            
def dfs_II(start, goal, N):
    frontier = [start]
    visited = set()

    distance = {}

    for i in range(1, N + 1):
        distance[i] = float('inf')
    
    distance[start] = 0

    while (frontier != []):
        current_state = frontier.pop()
        visited.add(current_state)

        if (current_state == goal):
            return distance[current_state]
        
        neighbours = successor(current_state)

        for neigh in neighbours:
            if (neigh not in visited):
                distance[neigh] = min (distance[neigh], distance[current_state] + 1)
                frontier.append(neigh)


from collections import deque

def bfs(start, goal):
    frontier = deque([(start, 0)])
    visited = set()

    while (len(frontier) != 0):
        current_state = frontier.popleft()
        visited.add(current_state[0])

        if (current_state[0] == goal):
            return current_state[1]
        
        neighbours = successor(current_state)

        for neigh in neighbours:
            if (neigh not in visited):
                frontier.append((neigh, current_state[1] + 1))