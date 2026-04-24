def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        if letter not in guesses:
            guesses.append(letter)

        display = ""
        all_guessed = True

        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"
                all_guessed = False

        print(display)
        print(all_guessed)

        return all_guessed

    return hangman_closure


def play_game(game):
    guess = input("Enter a letter: ")
    
    
    if game(guess):
        print("You guessed the word!")
        return
    else:
        play_game(game)


secret_word = input("Enter the secret word: ")
game = make_hangman(secret_word)
play_game(game)