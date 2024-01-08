def Rotating_letters(s):
    letter_list = ["I","O","S","H","Z","X","N"]
    full_or_not = 0
    for c in s :
        if c in letter_list:
            full_or_not += 1
  
    if full_or_not == len(s):
        return "YES"
    else:
        return "NO"
    
def Take_input():
    s = input()
    return s
s = Take_input()
print(Rotating_letters(s))