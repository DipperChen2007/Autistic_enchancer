def Party_Invitation(party_people,rounds):

    for round_position_inlist in rounds:
        round_position = 0
        
        
        while round_position < len(party_people):
            round_position += round_position_inlist
            
            party_people[round_position] = 0
        
        for i in range(len(party_people)):
            if party_people[i] == 0:
                party_people.pop(party_people[i])
    
    return party_people
    

def Take_input():
    person_number = int(input())
    party_people = []
    rounds = []
    for i in range(person_number):
        party_people.append(i)
    round_number = int(input())
    for round_n in range(round_number):
        rounds.append(int(input()))
    return party_people, rounds

party_people, rounds = Take_input()
print(Party_Invitation(party_people,rounds))