def pie_day(pie,person):
    if pie == person or person == 1:
        return 1
    elif pie < person:
        return 0
    answer = pie_day(pie-1,person-1) + pie_day(pie - person,person)
    return answer 
    
def Take_input():
    pie = int(input())
    person = int(input())
    return pie,person

pie,person = Take_input()
print(pie_day(pie,person))
