def Assigning_Partners(n,row_1,row_2):
    dic_1 = {}
    
    for i in range(n):
        if row_1[i] not in dic_1:
            dic_1[row_1[i]] = [row_2[i]]
        elif row_1[i] in dic_1:
            dic_1[row_1[i]].append(row_2[i])
        
    
    for i_1 in range(n):
        for i_2 in range(len(dic_1[row_1[i_1]])):
            if  row_1[i_1] not in dic_1[dic_1[row_1[i_1]][i_2]]:
                return "bad"
            if row_1[i_1] in dic_1[row_1[i_1]]:
                return "bad"
    
    return "good"

def Take_input():
    n = int(input())
    row_1=((input().split()))
    row_2=((input().split()))
    return n,row_1,row_2

n,row_1,row_2 = Take_input()
print(Assigning_Partners(n,row_1,row_2))
