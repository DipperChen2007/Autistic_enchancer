def Next_in_line(n_1,n_2):
    return n_2 + (n_2 - n_1)

def Take_input():
    n_1 = int(input())
    n_2 = int(input())
    return n_1,n_2
n_1,n_2 = Take_input()
print(Next_in_line(n_1,n_2))