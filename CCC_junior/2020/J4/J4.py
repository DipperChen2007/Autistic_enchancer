def Cyclic_Shifts(str_1,str_2):
    shifts = []
    for i in range(1,len(str_2)):
        shifts.append(str_2[i:len(str_2)] + str_2[0:i])
    for shift in shifts:
        if shift in str_1:
            return "yes"
        
    return "no"
        
def Take_input(): 
    str_1 = input()
    str_2 = input()
    return str_1,str_2

str_1,str_2 = Take_input()
print(Cyclic_Shifts(str_1,str_2))
