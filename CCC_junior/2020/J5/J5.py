from collections import defaultdict, deque
from sys import stdin

input = stdin.readline

def takeinput():
  row = int(input())
  col = int(input())
  dictionary = defaultdict(list)
  matrix = []
  
  for i in range (row):
    line = list(map(int, input().split()))
    for j in range(col):
      dictionary[line[j]].append((i+1, j+1))
    matrix.append(line)
  return matrix, dictionary

def BFS(start,goal,dictionary,matrix):
  frontier = deque([(len(matrix),len(matrix[0]))])
  visited = set()
  
  while len(frontier) != 0:
    current_state = frontier.popleft()
    visited.add(current_state)
    nextNum = current_state[0]*current_state[1]

    if nextNum == goal:
      return "yes"

    neighbours = dictionary[nextNum]

    for neighbour in neighbours:
      if neighbour not in visited:
        frontier.append(neighbour)
  return "no"

def escapeRoom(matrix,dictionary):
  goal = matrix[0][0]
  start = matrix[-1][-1]
  return BFS(start,goal,dictionary,matrix)

matrix, dictionary = takeinput()
print(escapeRoom(matrix,dictionary))