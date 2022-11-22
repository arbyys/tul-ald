import sys


def segmentsToNumber(segments):
    segments = ''.join(sorted(segments))
    if segments == 'abcdef':
        return 0
    elif segments == 'bc':
        return 1
    elif segments == 'abdeg':
        return 2
    elif segments == 'abcdg':
        return 3
    elif segments == 'bcfg':
        return 4
    elif segments == 'acdfg':
        return 5
    elif segments == 'acdefg':
        return 6
    elif segments == 'abc':
        return 7
    elif segments == 'abcdefg':
        return 8
    elif segments == 'abcdfg':
        return 9


def getSegments(time, clock):
    if (time == "broken"):
        return ""
    time = time.split(":")
    hours = time[0]
    minutes = time[1]
    seconds = time[2]
    returnString = ""
    if (clock == 1):
        returnString += ("a" if hours in ["09", "21"]
                         else ("b" if hours in ["06", "18"] else ""))
        returnString += ("a" if minutes == "45"
                         else ("b" if minutes == "30" else ""))
        returnString += ("a" if seconds == "45"
                         else ("b" if seconds == "30" else ""))
    elif (clock == 2):
        returnString += ("d" if hours in ["09", "21"]
                         else ("c" if hours in ["00", "12"] else ""))
        returnString += ("c" if minutes == "00"
                         else ("d" if minutes == "45" else ""))
        returnString += ("c" if seconds == "00"
                         else ("d" if seconds == "45" else ""))
    elif (clock == 3):
        returnString += ("g" if hours in ["03", "15"] else ("f" if hours in [
            "00", "12"] else ("e" if hours in ["06", "18"] else "")))
        returnString += ("f" if minutes == "00"
                         else ("g" if minutes == "15" else ("e" if minutes == "30" else "")))
        returnString += ("f" if seconds == "00"
                         else ("g" if seconds == "15" else ("e" if seconds == "30" else "")))
    return ''.join(set(returnString))

outputString = ""
resultSegments = ""
currentClock = 1

for line in sys.stdin:
    line = line.strip()
    if (line == '-'):
        continue
    elif (line == '---'):
        break
    resultSegments += getSegments(line.split(" ")[1], currentClock)
    currentClock += 1
    if ('clock-3' in line):
        outputString += str(segmentsToNumber(resultSegments))
        resultSegments = ""
        currentClock = 1

print(outputString)
