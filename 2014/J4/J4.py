def Wait_Time (n,lst):
    person_list = []
    person_wait_time = []
    for i in range(n):
        if lst[i][0] == "R":
            if (lst[i][1]) not in person_list:
                person_list.append((lst[i][1]))
                
    for i_2 in range(len(person_list)):
        first_position = lst.index(["R",person_list[i_2]])
        wait_time = 0
        
        while first_position <= n- 1:
            
            if lst[first_position][0] == "R":
                wait_time += 1
                first_position += 1
            elif lst[first_position][0] == "S":
                wait_time += 1
                first_position += 1
            elif lst[first_position][0] == "W":
                wait_time += int(lst[first_position][1])
                first_position += 2
        
        person_wait_time.append(str(wait_time))
        
    for i_4 in range(len(person_list)):
        print(person_list[i_4] + " " + person_wait_time[i_4])
    
    
def Take_input():
    lst = []
    n = int(input())
    for _ in range(n):
        lst.append(input().split())
    return n,lst

n,lst = Take_input()
Wait_Time (n,lst)