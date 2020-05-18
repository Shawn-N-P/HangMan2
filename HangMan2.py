import random

letters = []  # Creates a list that holds all correct guesses the user makes
Attempts = 1  # Attempts made by User. Maybe should have a reset when user wins or loses?
WordBank = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine"]  # List that contains all words for game
word = random.choice(WordBank)  # Chooses a random word from word bank
counter = 0

print("Welcome to Hang Man!")
print("You have 10 attempts to guess the word I'm thinking of... \n")


def compare(letter, chosen, count):  # Compares letter to the letters in chosen word if any match
    for x in range(0, len(word)):
        # print(count)
        # count += 1
        if letter == chosen[x]:
            return "You got it! \n"
        if x == len(chosen):
            return "Incorrect! \n"


while True:  # Allows user input and gives results output
    # print(word)  # Prints word for testing purposes only
    guess = input('Please guess a letter ')  # User guesses letter
    print(" ")  # Prints an extra line after the user guesses letter
    getAnswer = compare(guess, word, counter)
    print(str(Attempts) + " Attempts made. \n")
    if getAnswer == "You got it! \n":  # If the user guess letter input is correct
        letters.append(guess)
        print("Your guess {} was correct.".format(guess))
        print("Your guesses so far: " + str((", ".join(letters))))
    else:
        print("Your guess {} was incorrect. \n".format(guess))
        Attempts += 1
    if guess == word:  # If the user guesses the chosen word correctly
        print("You guessed the correct word! You won! \n")
    if Attempts == 10:  # If Attempts hit 10 then the game ends
        print("You lose! \n")
        break
