import sys
for line in sys.stdin:
    line = line.lower().rstrip()
    if (line == line[::-1]):
        print("ano")
    else:
        print("ne")
