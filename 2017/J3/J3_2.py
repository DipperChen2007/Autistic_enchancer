def Exactly_Electrical (point_1,point_2,electric):
    minimum_distance = abs(point_1[0]-point_2[0]) + abs(point_1[1]-point_2[1])
    if minimum_distance >0 :
        if electric > minimum_distance:
            if minimum_distance % 2 == 0:
                if electric % 2 == 0:
                    return "Y"
                else:
                    return "N"
            else:
                if electric % 2 == 0:
                    return "N"
                else:
                    return "Y"
       
            
    
        elif electric == minimum_distance:
            return "Y"
        
        else:
            return "N"
    elif minimum_distance == 0:
        if electric % 2 == 0:
            return "Y"
        else:
            return "N"
        
        
        
    
def Take_input():
    point_1 = list(map(int,input().split()))
    point_2 = list(map(int,input().split()))
    electric = int(input())
    return point_1,point_2,electric

point_1, point_2, electric = Take_input()
print(Exactly_Electrical (point_1,point_2,electric))