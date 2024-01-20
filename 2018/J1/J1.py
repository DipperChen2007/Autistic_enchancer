def Telemarketer_or_not (lst):
    if lst[0] in [8,9] and lst[3] in [8,9]:
        if lst[1] == lst[2]:
            return "ignore"
        else:
            return "answer"
    else:
        return "answer"
            

def Take_input():
    lst = []
    for _ in range(4):
        lst.append(int(input()))
    return lst

lst = Take_input()
print(Telemarketer_or_not (lst))