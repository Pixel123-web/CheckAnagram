# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(sorted(word.lower()) == sorted(anagram.lower())):
            print("They are anagrams")
            return True
            
    else:   
            print("Not  anagrams")
            return False

word = input(("enter first word: "))
anagram = input(("enter second word: "))
find_anagram(word , anagram)