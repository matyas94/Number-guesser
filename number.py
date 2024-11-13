import random
import time
import os
os.system('cls')
egyenleg = 100
jatek = input("Mit szeretnél játszan? (number guesser)\n")
ujra = "y"
while jatek == "number guesser" and ujra == "y":
    os.system('cls')
    print(f"Egyenleg: {egyenleg}\n")
    print("Gondolj egy számra egytől tízig.")
    time.sleep(2)
    os.system('cls')
    print(f"Egyenleg: {egyenleg}\n")
    bet = int(input("Mennyit szeretnél rakni? "))

    while bet > egyenleg:
        print("Nem tudsz ennyit rakni.")
        bet = int(input("Mennyit szeretnél rakni? "))
    wins = 0
    time.sleep(0.2)
    os.system('cls')
    for i in range(1,11):
        print(f"Egyenleg: {egyenleg}\n")
        gondolat = input(f"A szám amire gondoltál a(z) {i}?(y/n) ")
        if gondolat == "y":
            win = i
            wins += 1
        time.sleep(0.3)
        os.system('cls')

    if wins > 1:

        print(f"Egyenleg: {egyenleg}\n")
        print("Több számra nem gondolhatsz, vesztettél.")
    elif wins == 0:
        print(f"Egyenleg: {egyenleg}\n")
        print("Hazudsz, nem tudsz nem gondolni számra, vesztettél.")
    else:
        print(f"Egyenleg: {egyenleg}\n")
        print(f"A te számod: {win}, kitaláltam, vesztettél.")
    ujra = input("\nSzeretnél még játszani?(y/n)\n")   