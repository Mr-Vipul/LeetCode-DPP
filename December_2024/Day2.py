"""1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence"""

def prefixStart(sentence, searchWord):
    st = sentence.split(" ")
    n = len(searchWord)
    
    for index, word in enumerate(st):
        if word[:n]==searchWord:
            return index+1
    return -1


sentence = str("i love eating burger")
searchWord = str("burg")
print(prefixStart(sentence,searchWord))