def Vote_Count(v,tie):
    A = 0
    B = 0
    for i in range(v):
        if tie[i] == "A":
            A += 1
        elif tie[i] == "B":
            B += 1
            
    if A < B:
        return "B"
    elif B < A:
        return "A"
    else:
        return "Tie"
    
def Take_input():
    
    v = int(input())
    tie = input()
    return v,tie
v,tie = Take_input()
print(Vote_Count(v,tie))