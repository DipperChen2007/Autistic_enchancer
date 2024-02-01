
def Triangle_Times(degree_1,degree_2,degree_3):
    if degree_1 + degree_2 + degree_3 == 180:
        if degree_1 == 60 and degree_2 == 60 and  degree_3 == 60:
            return "Equilateral"
        elif degree_1 == degree_2:
            return "Isosceles"
        elif degree_3 == degree_2:
            return "Isosceles"
        elif degree_3 == degree_1:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Error"
    
def  Take_input():
    degree_1 = int(input())
    degree_2 = int(input())
    degree_3 = int(input())
    return degree_1,degree_2,degree_3

degree_1,degree_2,degree_3 = Take_input()
print(Triangle_Times(degree_1,degree_2,degree_3))