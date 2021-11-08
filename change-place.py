def change_place(thelist, start, destiny):

    print('Conditions test...')

    if len(thelist) < 2:
        print('[test error] list is too short')
        exit()

    if 0 > start or start >= len(thelist):
        print('[test error] element place isn\'t correct')
        exit()

    if 0 > destiny or destiny >= len(thelist):
        print('[test error] destination isn\'t correct')
        exit()

    print('Condition test finished')
    print('Changing place...')

    try:

        if destiny == 0:
            sttd = thelist[: start] + thelist[start+1:]
            # start to destiny
            thelist[0] = thelist[start]
            thelist[1:] = sttd

    except IndexError:

        if destiny == 0:
            sttd = thelist[:start]
            thelist[0] = thelist[start]
            thelist[1:] = sttd

    try:

        if destiny == (len(thelist)-1):
            sttd = thelist[:start] + thelist[start+1:]
            thelist[-1] = thelist[start]
            thelist[:-1] = sttd

    except IndexError:

        if destiny == (len(thelist)-1):
            sttd = thelist[start+1:]
            thelist[-1] = thelist[start]
            thelist[: -1] = sttd

    # SOL and EOL finished
    # Start Of Line

    if 0 < destiny < (len(thelist)-1):

        sttd = thelist[: start] + thelist[start+1: destiny+1]
        thelist[destiny] = thelist[start]
        thelist[: destiny] = sttd

    return thelist


x = input('Condition? ')

while x != 'end':
    c = input('list start destiny: ')
    c = c.strip().split()

    mylist = list(c[0])
    start = int(c[1])
    destiny = int(c[2])

    print(change_place(mylist, start, destiny))
    x = input('Condition? ')
