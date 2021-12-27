# We will have a secret word that the user can keep
# guessing until they get it correct.

secret_word = "giraffe"
guess = ""
guess_count = 0
max_guesses = 3
out_of_guesses = False

while guess != secret_word:
    guess = input("Input a word to guess: ")
    guess_count += 1
    if guess_count >= max_guesses and guess != secret_word:
        print("You suck.")
        out_of_guesses = True
        break

if not out_of_guesses:
    print("Congratulations")

