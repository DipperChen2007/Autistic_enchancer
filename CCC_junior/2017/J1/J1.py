def Quadrant_Selection (x,y):
    if x > 0 and y > 0:
        return "1"
    elif x > 0 and y < 0:
        return "4"
    elif x < 0 and  y > 0:
        return "2"
    elif x < 0  and y < 0:
        return "3"
    else:
        return "0"
    
def Take_input():
    x = int(input())
    y = int(input())
    return x,y

x,y = Take_input()
print(Quadrant_Selection (x,y))