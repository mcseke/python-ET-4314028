hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    if len(hexNum) > 3 or not isHexaStr(hexNum):
        return None

    dec = 0
    i = len(hexNum) - 1
    j = 0
    multiplier = {0: 1, 1: 16, 2: 16 * 16}
    while i >= 0:
        dec = dec + hexNumbers.get(hexNum[i]) * multiplier.get(j)
        i = i - 1
        j = j + 1
    return dec

def isHexaStr(hex):
    if type(hex) != str:
        return False
    for i in hex:
        if not i in hexNumbers:
            return False
    return True