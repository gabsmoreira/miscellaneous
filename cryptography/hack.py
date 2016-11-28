#Caesar Cipher

message = input('Enter text:')

words = []

for key in range (26):
    key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    words.append(translated)
    #print('translated:',translated)

    ## Check english


trns = []

dictionaryFile = open('dictionary.txt')

lines = dictionaryFile.read().split('\n')


for i in range(len(words)):
    if words[i].upper() in lines:
        trns.append(words[i])



dictionaryFile_pt = open('palavras.txt')

lines_pt = dictionaryFile_pt.read().split('\n')


for i in range(len(words)):
    if words[i].upper() in lines_pt:
        trns.append(words[i])


dictionaryFile_pt.close()


done = ''.join(trns)


print('Cypher:',done)
