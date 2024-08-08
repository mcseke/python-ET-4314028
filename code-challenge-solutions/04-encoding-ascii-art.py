def encodeString(stringVal):
    prevChar = stringVal[0]
    charCount = 0
    encodedString = []

    for ch in stringVal:
        if ch != prevChar:
            encodedString.append((prevChar, charCount))
            prevChar = ch
            charCount = 0
        charCount = charCount + 1
    encodedString.append((prevChar, charCount))
    return encodedString

def decodeString(encodedList):
    result = ""
    for key, value in encodedList:
        result = result + key * value
    return result
