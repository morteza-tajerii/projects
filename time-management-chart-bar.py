import matplotlib.pyplot as plt
import mysql.connector

print('connecting to mysql')

cnx = mysql.connector.connect(user='test', password='00000000',
                              host='127.0.0.1',
                              database='time_management')

print('connected to mysql')

cursor = cnx.cursor()

print('cursor created')

cursor.execute('SELECT * FROM wake_up;')

wake_ups = [x for x in cursor]

print(wake_ups)

for a, b, c in wake_ups:
    print("%i\n%s\n%s\n" % (a, str(b), str(c)))

dates = [str(b) for a, b, c in wake_ups]
times = []
for a, b, c in wake_ups:
    lst = str(c).split(':')
    time = (float(lst[2])+float(lst[1])*60+float(lst[0])*3600)
    times.append(time)

plt.plot(dates, times)
plt.title('wake up graph')
plt.xlabel('day')
plt.ylabel('time')
plt.show()
