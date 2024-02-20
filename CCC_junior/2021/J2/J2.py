def Take_input():
    n = int(input())
    lst = []
    for _ in range(n):
        name = input()
        price = int(input())
        lst.append([name,price])
    return n,lst

def S_A(n,lst):
    biggest = 0
    winner = ""
    for i in range(n):
        if lst[i][1] > biggest:
            biggest = lst[i][1]
            winner = lst[i][0]
    return winner

n,lst = Take_input()
print(S_A(n,lst))
        
        