import sys

dictWords = {}
dictPhrases = {}

words = []
for line in sys.stdin:
    line = line.strip()
    if (line == "" or line == " "):
        continue
    line = line.lower().strip()
    words.extend(line.split())

for index, word in enumerate(words):
    if (word == ""):
        continue
    if (word not in dictWords):
        dictWords[word] = 1
    else:
        dictWords[word] += 1

    if (index != 0):
        phrase = "{0} {1}".format(words[index-1], word)
        if (phrase not in dictPhrases):
            dictPhrases[phrase] = 1
        else:
            dictPhrases[phrase] += 1

totalWords = sum(dictWords.values())
totalPhrases = sum(dictPhrases.values())

dictWords = sorted(dictWords.items(), key=lambda x: x[1], reverse=True)
dictPhrases = sorted(dictPhrases.items(), key=lambda x: x[1], reverse=True)

resultString = "Word Frequency:\n"

for index, item in enumerate(dictWords):
    if (index >= 15):
        break
    resultString += " - {0}{1}% ({2})\n".format(item[0].ljust(
        13), '{:.2f}'.format(item[1]/totalWords * 100, 2), item[1])

resultString += "Phrase Frequency:\n"

for index, item in enumerate(dictPhrases):
    if (index >= 15):
        break
    resultString += " - {0} {1}% ({2})\n".format(item[0].ljust(
        20), '{:.2f}'.format(item[1]/totalPhrases * 100, 2), item[1])

print(resultString.rstrip('\n'))
