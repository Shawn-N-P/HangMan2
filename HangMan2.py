import random

letters = []
Tries = 5
Attempts = 0
WordBank = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  # List that contains all
# words for game 
word = random.choice(WordBank)  # Chooses a random word from word bank
count = 0
place = 0

print("Welcome to Hang Man")
print("Guess each letter of the word I'm thinking of.")


def compare(letter, chosen, rounds):  # Compares letter to the letters in chosen word if any match
    for x in range(0, len(chosen)):
        rounds = rounds + 1
        if letter == word[x]:
            return "You got it! \n"
        elif rounds == len(word):
            return "Incorrect! \n"


while True:  # Allows user input and gives information output
    print(word)
    guess = input('Please guess a letter ')  # User guesses letter
    print(" ")
    Attempts += 1
    getAnswer = compare(guess, word, count)
    print(getAnswer)
    print(str(Attempts) + " Attempts made.")
    if guess == word:
        print("You won!")
    if getAnswer == "You got it! \n":  # The letter guess input from users is correct
        letters.append(guess)
        print("Your guess {} was correct. ".format(guess))
        print("Your guesses so far, " + str((letters[0:])))
    if getAnswer == "Incorrect! \n":  # The letter guess input from users is incorrect
        Tries -= 1
        print("Your tries left: " + str(Tries))
    if Tries == 0:  # If tries hit 0 then the game ends
        break
