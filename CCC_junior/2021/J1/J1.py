def B_W (i):
    print(5*i - 400)
    if i < 100:
        print(1)
    elif i == 100:
        print(0)
    else:
        print(-1)
    
def Take_input():
    i = int(input())
    return i

i = Take_input()
B_W(i)