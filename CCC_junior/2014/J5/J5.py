def Assigning_Partners(n,row_1,row_2):
    dic  = {}
    for i in range(n):
        dic[row_1[i]] = row_2[i]
        pass

def Take_input():
    n = int(input())
    row_1=((input().split()))
    row_2=((input().split()))
    return n,row_1,row_2

print(Take_input())
