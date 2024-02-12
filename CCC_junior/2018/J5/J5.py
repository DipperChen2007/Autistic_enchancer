def successor(current_state,pages):
    neighbours = []
    for i in range(len(current_state)):
        neighbours.append(pages[current_state[i] - 1])
    return neighbours

from collections import deque

def BFS(start,goal,pages):
    YorN = ""
    answer = ""
    frontier = deque([(start,1)])
    visited = []
    for i in range(len(pages)):
        if 0 in pages[i]:
            YorN += "Y"
        else: 
            answer += "N"    

    while len(frontier) != 0:
        current_state = frontier.pop()
        if current_state[0] not in visited:
            visited.append(current_state[0])
        if goal in current_state[0]:
            answer += str(current_state[1])
            
        neighbours = successor(current_state[0],pages)
        
        for neighbour in neighbours:
            if neighbour not in visited:
                frontier.append((neighbour,current_state[1]+1))
    
    if YorN == "Y":
        print(YorN)
        print(answer)
    elif YorN == "N":
        print(YorN)


def Take_input():
    n = int(input())
    pages = []
    for _ in range(n):
        pages.append(list(map(int,input().split())))
    start = pages[0]
    goal = 0
    return pages,start,goal

pages,start,goal = Take_input()
BFS(start,goal,pages)