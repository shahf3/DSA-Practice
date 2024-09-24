def reverseString(sentance):
    sentance = sentance.split(".")


    return ".".join(sentance[::-1])

word = 'i.like.this.program.very.much'
print(reverseString(word))