# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


def minion_game(string):
    stuartResult = 0
    kevinResult = 0
    stringLength = len(string)
    for idx in range(0, stringLength):
        char = string[idx]
        if char in "AEIOU":
            kevinResult += (stringLength - idx)
        else:
            stuartResult += (stringLength - idx)
    
    if stuartResult < kevinResult:
        print('Kevin {kevinResult}'.format(kevinResult = kevinResult))
    elif stuartResult > kevinResult:
        print('Stuart {stuartResult}'.format(stuartResult = stuartResult))  
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)