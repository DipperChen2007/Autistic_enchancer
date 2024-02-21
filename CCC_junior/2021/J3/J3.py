def S_I(lst):
    answer = []
    for i in range(len(lst)):
        if lst[i] != "99999":
            ft = lst[i][0] + lst[i][1]
            if ft != "00":
                if (int(lst[i][0]) + int(lst[i][1]))%2 ==0:
                    answer.append(["right" + " " + lst[i][2:5]])
                elif (int(lst[i][0]) + int(lst[i][1]))%2 == 1:
                    answer.append(["left" + " " + lst[i][2:5]])
            else:
                if (int(lst[i-1][0]) + int(lst[i-1][1]))%2 ==0:
                    answer.append(["right" + " " + lst[i][2:5]])
                elif (int(lst[i-1][0]) + int(lst[i-1][1]))%2 == 1:
                    answer.append(["left" + " " + lst[i][2:5]])

    for i in range(len(answer)):
        print(" ".join(answer[i]))
        
def Take_input():
    lst = []
    lst.append(input())
    while lst[-1] != "99999":
        lst.append(input())
    return lst

lst = Take_input()
S_I(lst)