import hangman_creator

hangman = hangman_creator.Hangman(
    'C:\\Users\\1999p\\Desktop\\Hangman\\wordlists.txt')
hangman.ChooseTheWord()
hangman.LetterRandomlyGivenAlreadyStatus()

while True:
    hangman.GetFillWordStatus()
    hangman.GuessTheLetterInWordGiven()

    if(hangman.NumberOfAttemptsLeft == 0):
        print("{}, you're out of attempts! Game over !! The word was {}.".format(
            hangman.nameofThePlayer, hangman.ChosenWord))
        break

    elif (hangman.ChosenWord == ''.join(hangman.currentWordStatus)):
        print("Hurray! You won the Game {}!! The word was chosen which you've guessed correctly is :{}.".format(
            hangman.nameofThePlayer, hangman.ChosenWord))
        break
