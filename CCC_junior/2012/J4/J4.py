def shift_character(c, S):
    shift_value = (ord(c) - S)
    pos_in_alpha = (ord('Z') - shift_value) % 26

    return chr(ord('Z') - pos_in_alpha)

def big_bang_secrets(K, s):
    rtn, pos = "", 1

    for c in s:
        S = 3 * pos + K
        rtn += shift_character(c, S)
        pos += 1
    
    return(rtn)

def Take_input():
    n = int(input())
    s = input()
    return n , s

n,s = Take_input()
