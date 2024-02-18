def Tandem_bicycle(q,c,row_1,row_2):
    answer = 0
    if q == 1:
        row_1.sort()
        row_2.sort()
        for i_1 in range(c):
            if row_1[i_1] <= row_2[i_1]:
                answer += row_2[i_1]
            elif row_1[i_1] >= row_2[i_1]:
                answer += row_1[i_1]
    
    if q == 2:
        al_row = []
        for i in range(c):
            al_row.append(row_1[i])
            al_row.append(row_2[i])
        al_row.sort()
        for i in range(c):
            answer += al_row[::-1][i]
    
    return answer

def Take_input():
    q = int(input())
    c = int(input())
    
    row_1 = list(map(int,input().split()))
    row_2 = list(map(int,input().split()))
    return q,c,row_1,row_2

q,c,row_1,row_2 = Take_input()
print(Tandem_bicycle(q,c,row_1,row_2))