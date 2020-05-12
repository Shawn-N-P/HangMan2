import random

Tries = 5
Attempts = 0
WordBank = ["zero", "one", "two", "three", "four", "five"]  # List that contains all words for game
word = random.choice(WordBank)  # Chooses a random word from word bank
letters = []
output = ""

print("Welcome to Hang Man")
print("Guess each letter of the word I'm thinking of.")


def compare(letter, chosen, out, rounds=0):  # Compares letter to the letters in chosen word if any match
    for x in range(0, len(chosen)):
        print("Value of Rounds(1): " + str(rounds))
        rounds = rounds + 1
        print("Value of Rounds(2): "+str(rounds))
        print(chosen[x])
        print(chosen)
        out += letter
        if letter == chosen[x]:
            letters.append(letter)
            print("You got it")
            print("Your guess {} was correct. ".format(guess))
            print("Your guesses so far, " + str((letters)))
            print("This is the extra output: "+str(out))
            return out
        if rounds == len(chosen):
            print("Incorrect!")
            return 1


while True:  # Allows user input and gives information output
    guess = input('Please guess a letter ')  # User guesses letter
    Attempts += 1
    answer = compare(guess, word, output)

    if answer == 1:
        Tries = Tries - 1
        print("Your tries left: " + str(Tries))

    if Tries == 0:  # If tries hit 0 then the game ends
        break
