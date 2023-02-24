

def stringToLines(string):
    lines = []
    currLine = ""
    for letter in string:
        if letter in [";", "\n"]:
            lines.append(currLine)
            currLine = ""
        else:
            currLine += letter
    lines.append(currLine)
    return lines