def Happy_Sad (s):
    ha = s.count(":-)")
    sa = s.count(":-(")
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