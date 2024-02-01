def check_if_favourite(lst):
    if lst[0] == 0:
        if lst[1] - lst[2] == lst[2] - lst[3]:
            return True
        else:
            return False
    else:
        if lst[0] - lst[1] == lst[1] - lst[2] and lst[1] - lst[2] == lst[2] - lst[3]:
            return True
        else:
            return False
def Favourite_Times (n):
    answer = 0
    day = n // 720
    if day == 0:
        day = day
    elif day > 0:
        n = n - day * 720 
        answer += 31 * day
    start_point = [1,2,0,0]
    while n > 0:
        start_point[-1] += 1
        if start_point[-1] == 10:   #[1,2,5,10]
            start_point[2] += 1
            start_point[-1] = 0     #[1,2,6,0]
        elif start_point[0] == 0 and start_point[1] == 10: #[0,10,0,0]
            start_point[0] = 1
            start_point[1] = 0    #[1,0,0,0]         
        elif start_point[2] == 6:   #[1,2,6,0]
            start_point[1] += 1
            start_point[2] = 0      #[1,3,0,0]         
        elif start_point[0] == 1 and start_point[1] == 3: #[1,3,0,0]
            start_point[0] = 0 
            start_point[1] = 1     #[0,1,0,0]        
        if check_if_favourite(start_point):
            answer += 1
        n -= 1
    return answer
def Take_input():
    n = int(input())
    return n 
n = Take_input()
print(Favourite_Times (n))