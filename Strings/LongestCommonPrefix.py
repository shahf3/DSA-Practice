def LongestPrefix(sentance):
    if not sentance:
        return -1
    
    sentance.sort()

    first = sentance[0]
    last = sentance[-1]
    min_length = min(len(first), len(last))

    i=0
    while i < min_length and first[i] == last[i]:
        i += 1
    
    if i == 0:
        return -1

    return first[:i]

exam = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
print(LongestPrefix(exam))