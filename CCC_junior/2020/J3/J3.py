def art(lst):
    find_left = []
    find_right = []
    for i in range(len(lst)):
        find_left.append(lst[i][0])
        find_right.append(lst[i][1])
    x1 = min(find_left) - 1
    y1 = min(find_right) -1 
    x2=  max(find_left) + 1
    y2 = max(find_right) + 1
    print(str(x1) + "," + str(y1))
    print(str(x2) + "," + str(y2))
    
def Take_input():
    lst = []
    n = int(input())
    for _ in range(n):
        lst.append(list(map(int,input().split(","))))
    return lst

lst = Take_input()
art(lst)