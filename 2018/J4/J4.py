def check_line(lst):

 
  i = 1
  first = lst[0]
  while i < len(lst):
      second = lst[i]
      if second < first:
          return False
      first = second
      i += 1
  return True

def is_correct_orientation(matrix):
    for i in range(len(matrix)):
        if not check_line(matrix[i]):
            return False
        col = [matrix[j][i] for j in range(len(matrix[i]))] 
        if not check_line(col):
            return False

    return True

def rotate(matrix):
    pass

def Sunflower(n,matrix):
    while not is_correct_orientation(matrix):
        matrix = rotate(matrix)
    return matrix

def Take_input():
    matrix = []
    n = int(input())
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    return matrix

print(is_correct_orientation(Take_input()))
