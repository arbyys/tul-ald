import sys

dict = {}
all = []

for line in sys.stdin:
    line = line.rstrip()
    for number in line.split(","):
        if (number not in all):
            all.append(number)

        if (number not in dict.keys()):
            dict[number] = 1
        else:
            dict[number] += 1

moreThanOne = []
one = []
for item in all:
    if (dict[item] > 1 and item not in moreThanOne):
        moreThanOne.append(item)
    elif (dict[item] == 1 and item not in one):
        one.append(item)

print("all: {0}".format(','.join(all)))
print(">1x: {0}".format(','.join(moreThanOne)))
print("=1x: {0}".format(','.join(one)))
