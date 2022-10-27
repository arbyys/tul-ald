def mirrorFirstHalfToSecond(number):
    number = str(number)
    newString = number[0:int(len(number)/2)]
    for indexFromStart in range(int(len(number)/2), -1, -1):
        newString += number[indexFromStart]
    return newString


def isPalindromAndHigher(number, base):
    if ((str(number) == str(number)[::-1]) and (number > base)):
        return True
    return False


def findNearestPalindromNumber(number):
    return


print(mirrorFirstHalfToSecond(12600))

"""
while True:
    number = int(input(""))
    if (number == -1):
        break
    print(findNearestPalindromNumber(number))
"""

12922
