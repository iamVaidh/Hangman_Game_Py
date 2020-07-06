import random as r
import re


for lines in range(0, 80):
    print("==", end='')

print()

print("\t##     ##       #       ###     ## ########## ###      ###        #        ###     ##            ##########        #        ###       ### ##########", end='')
print("\t\t##     ##      ###      ## ##   ## ##      ## ## ##  ## ##      ## ##      ## ##   ##            ##      ##      ## ##      ## ##   ## ## ##")
print("\t#########     ## ##     ##  ##  ## ##      ## ##  ## ## ##     ##   ##     ##  ##  ##            ##      ##     ##   ##     ##  ## ##  ## ##")
print("\t#########    #######    ##   ## ## ##         ##   ##   ##    #########    ##   ## ##            ##            #########    ##   ##    ## ##########")
print("\t##     ##   ##     ##   ##    #### ##   ##### ##        ##   ##       ##   ##    ####            ##   #####   ##       ##   ##         ## ##")
print("\t##     ##  ##       ##  ##     ### ##   ## ## ##        ##  ##         ##  ##     ###            ##   ## ##  ##         ##  ##         ## ##")
print("\t##     ## ##         ## ##     ### ####### ## ##        ## ##           ## ##      ##            ####### ## ##           ## ##         ## ##########")

print()
for h2 in range(0, 80):
    print("==", end='')

print()


class Hangman:

    print("Enter your name :  ", end='')
    nameofThePlayer = str(input())

    def __init__(self, PathToWordlist):
        self.PathToWordlist = PathToWordlist
        self.NumberOfAttemptsLeft = 6
        self.currentLetterByUser = ''
        self.ChosenWord = ''
        self.guessed_letters = []

    def ChooseTheWord(self):
        WordlistFile = open(self.PathToWordlist)
        words = WordlistFile.read().split('\n')
        words_count = len(words)
        self.ChosenWord = words[r.randrange(0, words_count)]
        # print(self.ChosenWord)
        self.currentWordStatus = ['-' for j in range(len(self.ChosenWord))]

    def LetterRandomlyGivenAlreadyStatus(self):
        nos = r.randrange(1, 3)
        for i in range(nos):
            position = r.randrange(0, len(self.ChosenWord))
            self.currentWordStatus[position] = self.ChosenWord[position]

    def GuessTheLetterInWordGiven(self):
        letter = input("Guess the letter :")
        if(letter in self.guessed_letters):
            print("You've already guessed the letter ! Your guesses are : {}".format(
                ','.join(self.guessed_letters)))
            return

        self.guessed_letters.append(letter)
        occurrences = []
        occurrence = re.finditer(letter, self.ChosenWord)
        for m in occurrence:
            occurrences.append(m.start())

        if(len(occurrences) == 0):
            self.NumberOfAttemptsLeft -= 1
            print("Oops ! Your guess was wrong. Attempts remaining is {}".format(
                self.NumberOfAttemptsLeft))
        else:
            for position in occurrences:
                self.currentWordStatus[position] = self.ChosenWord[position]
            print("Correct word !")

    def GetFillWordStatus(self):
        print("Current status : {}\n".format(''.join(self.currentWordStatus)))
