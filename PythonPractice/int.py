chance = 0
maxlimit = 2
while (True):
    num = input('Enter a number: ')
    if (num.isnumeric()):
        continue
    elif (chance < maxlimit):
        print('Wrong input, you have ', maxlimit - chance, 'attempts left')
        chance += 1
        continue
    else:
        print('Exceeded limit')
        break
