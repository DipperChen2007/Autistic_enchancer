def closest_vowel(c):
    left_distance = 0
    right_distance = 0
    Vowels_distance = [ord("a"),ord("e"),ord("i"),ord("o"),ord("u")]
    left_copy = ord(c)
    right_copy = ord(c)
    special = ["x","y"]
    if c in special:
        return "u"
    
    else:
   
        while left_copy not in Vowels_distance:
            left_copy -= 1
            left_distance += 1
        while right_copy not in Vowels_distance:
            if right_copy != ord("z"):
                right_copy += 1
                right_distance += 1
            else:
                right_copy = ord("a")
                right_distance += 1
        if left_distance <= right_distance:
            return chr(ord(c) - left_distance)
        elif left_distance > right_distance:
            return chr(ord(c) + right_distance)
   
    
def Rovarspraket(english_word):
    rovarspraket_word = ""
    Vowels = ["a","e","i","o","u"]
   
    for c in english_word:
        
        if c in Vowels:
            rovarspraket_word += c
        elif c not in Vowels:
            closestvowel = closest_vowel(c)
            if c != "z":
                if chr(ord(c) + 1) not in Vowels:
                    rovarspraket_word += c + closestvowel + chr(ord(c) + 1)
                else:
                    rovarspraket_word += c + closestvowel + chr(ord(c) + 2)
            else:
                rovarspraket_word += "zuz"
    return rovarspraket_word


def Take_input():
    english_word = input()
    return english_word

english_word = Take_input()
print(Rovarspraket(english_word))