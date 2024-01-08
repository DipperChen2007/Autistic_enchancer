def Special_Day(n_1,n_2):
    if n_1 == 1:
        return "Before"
    elif n_1 == 2:
        if n_2 == 18:
            return "Special"
        elif n_2 < 18:
            return "Before"
        else:
            return "After"
    elif n_1 > 2:
        return "After"

def Take_input():
    n_1 = int(input())
    n_2 = int(input())
    return n_1,n_2
n_1,n_2 = Take_input()
print(Special_Day(n_1,n_2))