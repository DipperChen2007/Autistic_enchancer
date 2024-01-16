def check_more_than_a_day(number):
    day = 0
    if number > 12 * 60:
        while number > 12 * 60:
            number -= 12*60
            day += 1
        return day
    else:
        return day
    
def check_favourite(number): #2.1
    string_number = str(number)
    if number < 10:
        if len(string_number) == 3: #"2.1"
            string_number += "0" #"2.10"
            difference_0_and_2 = int(string_number[0]) - int(string_number[2])
            difference_2_and_3 = int(string_number[2]) -int(string_number[3])
            if difference_0_and_2 == difference_2_and_3:
                return True
            else:
                return False
        elif len(string_number) == 1:
            return False
        
        elif len(string_number) == 4: #"2.10"
            if difference_0_and_2 == difference_2_and_3:
                return True
            else:
                return False
    else: # number >= 10
        if string_number == "12.34" or string_number == "11.11":
            return True
        else:
            return False
            
def check_go_up(add_time):
    if add_time > 12:
        if add_time == 12.6:
            add_time = 1
            return add_time
        else:
            return add_time
    elif add_time - int(add_time) == 0.6:
        add_time = int(add_time) + 1
        return add_time
    else:
        return add_time 

def Favourite_Times(n): # 
    answer = 0
    day = check_more_than_a_day(n) 
    if day > 0:
        new_n = n - day * 12 * 60
        
    else:
        new_n = n
    new_n = new_n / 100 #0.34
    add_time = 12
    
    while new_n > 0: 
        add_time += 0.01
        add_time = check_go_up(add_time)
        
        if check_favourite(add_time) ==  True:
            answer += 1
            
        new_n -= 0.01
    return answer
    


def Take_input():
    n = int(input())
    return n 

n = Take_input()
print(Favourite_Times(n))