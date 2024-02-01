def check_digit(n):
    counter = [0] * 10

    for c in n:
        counter[ord(c) - ord('0')] += 1
        if (counter[ord(c) - ord('0')]) >= 2:
            return False
        
    return True

def from_1987_to_2013(n):
    n = str(int(n) + 1)
    
    while (check_digit(n) == False):
        n = str(int(n) + 1)
    
    print(n)

from_1987_to_2013('1023')