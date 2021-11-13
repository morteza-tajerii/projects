from os import listdir
import re

path = input('Please enter series path: ')
list_movies = sorted([f for f in listdir(path)])

print('Script is Working...')

for movie in list_movies:
    subject = re.findall(r'.*S\d{2}E(\d{2}).720p.*\.mkv', movie)
    list_movies[list_movies.index(movie)] = str(subject[0])

s = 0

print('Script fnished.')

for i in range(len(list_movies)+1):
    try:
        if int(list_movies[i]) == int(list_movies[i-1])+1:
            pass

        elif int(list_movies[i]) == 1:
            s += 1

        else:
            e = (int(list_movies[i])-1)
            print('E%i from S%i is NOT downloaded' % (e, s))

    except IndexError:
        pass

print('Bye :)')
