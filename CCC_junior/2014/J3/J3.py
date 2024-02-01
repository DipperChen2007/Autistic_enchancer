def Double_Dice (time,game):
    score_1 = 100
    score_2 = 100
    for i in range(time):
        if game[i][0] < game[i][1]:
            score_2 -= game[i][1]
        elif game[i][0] > game[i][1]:
            score_1 -= game[i][0]
        else:
            pass
    print(score_2)
    print(score_1)
    
         
def Take_input():
    game = []
    time = int(input())
    for _ in range(time):
        a,b = map(int, input().split())
        game.append([a,b])
    return time, game 
time,game = Take_input()
Double_Dice (time,game) 