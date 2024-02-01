def Hidden_Palindrome (s):
    biggest = len(s)
    while biggest > 0:
        for i in range(len(s) - biggest + 1):
            if s[i :i+biggest] == (s[i:i+biggest])[::-1]:
                return len(s[i:i+biggest])
        biggest -=1

def Take_input():
    s = input()
    return s
s = Take_input()
print (Hidden_Palindrome (s))


