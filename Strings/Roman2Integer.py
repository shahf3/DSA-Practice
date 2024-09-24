translation = {
    "I": 1, "V": 5, "X": 10, "L": 50, 
    "C": 100, "D": 500, "M": 1000
} 

def RomanToInteger(strings):
    translation = {
    "I": 1, "V": 5, "X": 10, "L": 50, 
    "C": 100, "D": 500, "M": 1000
    }

    res = 0
    i = 0
    while i < len(strings):
        if i + 1 < len(s) and translation[strings[i]] < translation[strings[i+1]]:
            res = res + (translation[strings[i+1]] - translation[strings[i]])
            i = i + 2
        else:
            res = res + (translation[strings[i+1]] + translation[strings[i]])
            i += 1
        
    return res

s = 'IX'
print(RomanToInteger(s))