def Epidemiology(lst):
    add = lst[1]
    answer = 0
    day = 0
    while answer <= lst[0]:
        answer +=  add
        add = add*lst[2]
        day += 1
    return day - 1

def Take_input():
    lst = []
    for _ in range(3):
        lst.append(int(input()))
    return lst

lst = Take_input()
print(Epidemiology(lst))