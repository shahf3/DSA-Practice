def panagram(word):

    alphas = 'abcdefghijklmnopqrstuvwxyz'
    word = word.lower()  # Convert the input to lowercase
    word = ''.join([char for char in word if char.isalpha()])  # Filter out non-alphabetic characters

    i = 0
    while i < len(alphas) and alphas[i] in word:
        i = i + 1
    
    if i == 26:
        return "panagram"
    else:
        return "not a panagram"cd

word1 = "The quick brown fox jumps over the lazy dog"
word2 = "The quick brown fox jumps over the dog"
print(panagram(word2))