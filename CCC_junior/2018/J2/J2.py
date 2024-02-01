def Occupy_parking (n,yesterday,today):
    answer = 0
    for i in range(len(yesterday)):
        if yesterday[i] == today[i] and yesterday[i] == "C":
            answer += 1
        
    return answer

def Take_input():
    n = int(input())
    yesterday = input()
    today = input()
    return n, yesterday, today
n,yesterday,today = Take_input()
print(Occupy_parking (n,yesterday,today))