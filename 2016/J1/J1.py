def Tournament_Selection(lst):
    w = 0
    for i in range(6):
        if lst[i] == "W":
            w += 1
    if w == 5 or w == 6:
        return "1"
    elif w == 3 or w == 4:
        return "2"
    elif w == 1 or w == 2:
        return "3"
    else:
        return "-1"

def Take_input():
    lst = []
    for _ in range(6):
        lst.append(input())
    return lst
lst = Take_input()
print (Tournament_Selection(lst))