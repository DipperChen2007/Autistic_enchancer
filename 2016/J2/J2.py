def helper(lst):
    answer = ""
    for i in range(8):
        if (i + 1) // 4 == 0:
            if lst[i] + lst[i+1] + lst[i+2] + lst[i+3] == lst[i + 4] + lst[i+1+4] + lst[i+2+4] + lst[i+3+4]:
                answer+="T"
            else:
                answer+="F"
    for i in range(3):
        if lst[i] + lst[i+4] + lst[i+8] + lst[i+12] ==  lst[i + 1] + lst[i+4 + 1] + lst[i+8+1] + lst[i+12+1]:
            answer+="T"
        else:
            answer+="F"
    return answer
def Magic_Squares(lst):
    for c in helper(lst):
        if c == "F":
            return "not magic"
        else:
            return "magic"
              

        
def Take_input():
    lst = []
    for _ in range (4):
        
        lst.append(list(map(int,(input().split()))))
    return lst
lst =   Take_input() 
print(Magic_Squares(lst))