from collections import deque
  
def bfs(start,book,N):
  frontier = deque([(start,0)])
  visited = set()
  distance = 0
  finished = False
  
  while (frontier != []):
    curstate = frontier.popleft()
    visited.add(curstate[0])
      
    neighbours = book[curstate[0]]
    if not finished and neighbours == []:
      distance = curstate[1] + 1
      finished = True
      
    for neigh in neighbours:
      if(neigh not in visited):
        frontier.append((neigh, curstate[1] + 1))
  return visited, distance

def takeInput():
  N = int(input())
  book = {}
  for i in range(N):
    line = [int(i) for i in input().split()]
    book[i+1] = line[1:]
  return book

def Choose_your_own_path(N, book):
  visited, distance = bfs(1, book, N)

  if len(visited) == N:
    print('Y')
  else:
    print('N')

  print(distance)

book = takeInput()