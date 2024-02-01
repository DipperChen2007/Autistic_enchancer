def  Icon_Scaling(i):
  result = ""
  for _ in range(i):
    result += ("*" * i + "x" * i + "*" * i + "\n")
  for __ in range(i):
    result += (" " * i + "x" * i + "x" * i + "\n")
  for ___ in range(i-1):
    result += ("*" * i + " " * i + "*" * i + "\n")
  result += ("*" * i + " " * i + "*" * i)
    
  return result

def Take_input():
  i = int(input())
  return i 

i = Take_input()
print(Icon_Scaling(i))