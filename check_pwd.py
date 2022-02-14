def check_pwd(pw):
    lowerCount = 0
    upperCount = 0
    digitCount = 0
    symbolCount = 0
    symbol = '~`!@#$%^&*()_+-='
    if 8 <= len(pw) <= 20:
        for x in range(len(pw)):
            if pw[x].islower():
                lowerCount += 1
            elif pw[x].isupper():
                upperCount += 1
            elif pw[x].isdigit():
                digitCount += 1
            elif pw[x] in symbol:
                symbolCount += 1
        if lowerCount > 0 and upperCount > 0 and digitCount > 0 and symbolCount > 0:
            return True
        else:
            return False
    else:
        return False

pw = 'ABCdef1234567'
print(check_pwd(pw))

