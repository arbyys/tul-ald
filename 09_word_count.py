import sys

text = ""
dictWords = {}
dictPhrases = {}

phrasesToAdd = 0

for line in sys.stdin:
    line = line.replace("\n", "")
    if (line == "" or line == " "):
        continue
    text += "{0} ".format(line.lower())

text = text.split(" ")
for index, word in enumerate(text):
    if (word == ""):
        continue
    if (word not in dictWords):
        dictWords[word] = 1
    else:
        dictWords[word] += 1

    if (index != 0):
        phrase = "{0} {1}".format(text[index-1], word)
        if (phrase[0] == " "):
            phrasesToAdd += 1
            continue
        if (phrase not in dictPhrases):
            dictPhrases[phrase] = 1
        else:
            dictPhrases[phrase] += 1

totalWords = sum(dictWords.values())
totalPhrases = sum(dictPhrases.values()) + phrasesToAdd

dictWords = sorted(dictWords.items(), key=lambda x: x[1], reverse=True)
dictPhrases = sorted(dictPhrases.items(), key=lambda x: x[1], reverse=True)

resultString = "Word Frequency:\n"

for index, item in enumerate(dictWords):
    if (index >= 15):
        break
    resultString += " - {0}{1}% ({2})\n".format(item[0].ljust(
        13), '{:.2f}'.format(round(item[1]/totalWords * 100, 2)), item[1])

resultString += "Phrase Frequency:\n"

for index, item in enumerate(dictPhrases):
    if (index >= 15):
        break
    resultString += " - {0}{1}% ({2})\n".format(item[0].ljust(
        21), '{:.2f}'.format(round(item[1]/totalPhrases * 100, 2)), item[1])

print(resultString.rstrip('\n'))
