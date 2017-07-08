from pygame import *

def playSound(filename):
    mixer.init(frequency=17000)
    sonido = mixer.Sound(filename)
    mixer.Sound.play(sonido)
    while mixer.get_busy():
        time.Clock().tick(10)

hours = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
        7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve'}

minutes = {0:'', 2:'twen', 3:'thir', 4:'for', 5:'fif', 6:'six', 7:'seven',
        8:'eigh', 9:'nine', 10: 'teen', 11:'ty'}

while True:
    print('Input an hour with the  24h format in the following way: xx:xx')
    hour = input().split(':')
    if int(hour[0]) > 24 or int(hour[1]) > 59:
        print('Error: Type an hour again\n')
        continue
    else:
        break

if int(hour[0]) < 12: day = 'am'
else: day = 'pm'

print("It's", end=' ')
playSound('its.wav')

if int(hour[0]) <= 12:
    playSound(str(int(hour[0]))+'.wav')
    print(hours[int(hour[0])], end=' ')
else:
    playSound(str(int(hour[0])-12)+'.wav')
    print(hours[int(hour[0])-12], end=' ')

if int(hour[1]) < 10:
    playSound('o.wav')
    print("o'", end=' ')
    playSound(str(int(hour[1]))+'.wav')
elif int(hour[1]) in range(10, 13):
    playSound(hour[1]+'.wav')
    print(hours[int(hour[1])], end=' ')
elif int(hour[1]) < 20:
    for i in range(3,10):
        if hour[1][1] == str(i):
            playSound(minutes[i]+'.wav')
            playSound('teen.wav')
            print(minutes[i]+'teen', end=' ')
else:
    for i in range(2,10):
        if hour[1][0] == str(i):
            for j in range(0,10):
                if hour[1][1] == str(j):
                     playSound(minutes[i]+'.wav')
                     if str(j) == '0':
                         playSound('ty.wav')
                     else:
                         playSound('ty'+str(j)+'.wav')
                     print(minutes[i]+"ty "+hours[j], end=" ")

playSound(day+'.wav')
print(day)
