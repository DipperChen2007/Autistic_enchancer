def Dog_Treats(lst):
    answer = 0
    answer = answer + lst[0]*1 + lst[1]*2 + lst[3]*3
    if answer >= 10:
        return "happy"
    else:
        return "sad"


def Take_input():
    lst = []
    for _ in range(3):
        lst.append(int(input()))
    return lst

lst = Take_input()
print(Dog_Treats(lst))