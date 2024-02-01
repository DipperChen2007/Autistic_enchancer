def Happy_Sad (s):
    ha =0
    sa =0
    
    for i in range (len(s) - 3):
        if s[i] + s[i+1] + s[i+2] == ":-)":
            ha+=1
        elif s[i] + s[i+1] + s[i+2] == ":-(":
            sa += 1
        else:
            pass
    
    if ha>sa:
        return "happy"
    elif sa>ha:
        return "sad"
    elif sa==ha and sa!=0:
        return "unsure"
    elif ha==0 and sa==0:
        return "none"
    
def Take_input():
    s = input()
    return s 
s = Take_input()
print (Happy_Sad (s))