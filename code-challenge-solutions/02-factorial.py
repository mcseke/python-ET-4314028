def factorial(num):
    if type(num) != int or num < 0:
        return None

    result = 1
    while num > 0:
        result = result * num
        num = num - 1
    return result