#guess the number game.
import random

secretNumber = random.randint(1,20)

print('tebak nomor yang akan keluar dari 1 sampai 20')

#beri kesampatan menebak 6 kali
for guessTaken in range(1, 7):
    print('tebakan ke ' + str(guessTaken))
    guess = int(input())
    if(guess < secretNumber):
        print('terlalu rendah')
    elif(guess > secretNumber):
        print('terlalu tinggi')
    else:
        break

if guess == secretNumber:
    print('benar!!!! nilainya adalah ' + str(guess) + ' kamu berhasil di percobaan ke ' + str(guessTaken))
else:
    print('maaf kamu berhasil silahkan ulangi')