# Sayı Tahmin Oyunu
from random import randint

easyLevelRight = 10
hardLevelRight = 5


def difficultyLevel():
    levelOption = input("Oyunun zorluğunu seçiniz. 'Kolay' veya 'Zor'\n").lower()
    if levelOption == 'kolay':
        print("Oyunu kazanabilmeniz için 10 hakkınız bulunmaktadır.")
        return easyLevelRight
    else:
        print("Oyunu kazanmak için 5 hakkınız bulunmaktadır.")
        return hardLevelRight


def guessingGame():
    print("Oyun Başlıyor! Bilgisayar 1-100 arasında bir sayı aklından tuttu.")
    computerGuess = randint(1, 100)
    remainingRight = difficultyLevel()

    while remainingRight > 0:
        yourGuess = int(input("Bilgisayarın aklından tuttuğu sayı nedir? "))

        if yourGuess > computerGuess:
            print("Büyük at da devler yesin :). Daha küçük bir sayı tahmin ediniz!\n")
            remainingRight -= 1
        elif yourGuess < computerGuess:
            print("Ufak at da civcivler yesin :). Daha büyük bir sayı tahmin ediniz!\n")
            remainingRight -= 1
        else:
            print("Tebrikler! Sayıyı doğru tahmin ettiniz!")
            break

        if remainingRight == 0:
            print("Oyun hakkınız kalmamıştır. Oyunu kaybettiniz!\n")
            newGame = input("Yeni bir oyun oynamaya ne dersiniz? 'Evet' veya 'Hayır': ").lower()

            if newGame == 'evet':
                guessingGame()
            else:
                print("Oyun sona erdi.")
                break


guessingGame()
