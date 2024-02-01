def Shifty_Sum (number,n):
    copy_number = number
    n_1 = 0
    while n_1 < n:
        copy_number += number * 10
        number = number*10
        n_1 += 1
    return copy_number

def Take_input():
    number = int(input())
    n = int(input())
    return number,n

number, n = Take_input()
print(Shifty_Sum (number,n))