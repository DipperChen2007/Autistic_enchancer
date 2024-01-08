def Party_Invitation(party_people,rounds):
    people_copy = party_people[:]
    for round_position_inlist in rounds:
        round_position = 0
        
        
        while round_position < len(people_copy):
            round_position += round_position_inlist
            
            party_people.remove(round_position)
            people_copy[round_position] = 0
        
        for i in people_copy:
            if people_copy[i] == 0:
                people_copy.remove(people_copy[i])
    
    return party_people
    

def Take_input():
    person_number = int(input())
    party_people = []
    rounds = []
    for i in range(person_number):
        party_people.append(i)
    round_number = int(input())
    for round_n in range(round_numebr):
        rounds.append(int(input()))
    return party_people, rounds

party_people, rounds = Take_input()
print(Party_Invitation(party_people,rounds))