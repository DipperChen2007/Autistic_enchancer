def Arrival_Time(time):
    distance = 120
    hour = int(time[0])
    minute = int(time[1])
    while distance > 0:
        
        if 7 <= hour < 10 or 15 <= hour < 19:
            distance -= 0.5
        else:
            distance -= 1
        minute += 1
    
        while minute>= 60:
            minute -= 60
            hour+=1
        while hour >= 24:
            hour -=24
            
    if hour< 10:
        print("0" + str(hour) ,end =  ":")
    else:
        print(str(hour),end =  ":")
    if minute < 10:
        print("0" + str(minute))
    else:
        print(str(minute))
        
def Take_input():
    time = (input().split(":"))
    return time
time = Take_input()
Arrival_Time(time)
