def Modern_art(r,c,choice_list):
    answer = 0
    row = [0] * r
    col = [0] * c
    for i in range(len(choice_list)):
        if choice_list[i][0] == "R":
            row[choice_list[i][1] - 1] += 1
        if choice_list[i][0] == "C":
            col[choice_list[i][1] - 1] += 1
    for i in range(r):
        for j in range(c):
            if (row[i] + col[j]) % 2 == 1:
                answer += 1
    return answer
        

def Take_input():
    r= int(input())
    c= int(input())
    choice = int(input())
    choice_lst = []
    for _ in range(choice):
        choice_l = input().split()
        choice_l[1] = int(choice_l[1])
        choice_lst.append(choice_l)
    return r,c,choice_lst

r,c,choice_lst = Take_input()
print(Modern_art(r,c,choice_lst))