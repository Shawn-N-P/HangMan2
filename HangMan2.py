import random

letters = []                                        # Creates a list that holds all correct guesses the user makes
Attempts = 0                                        # Attempts made by User. Maybe should have a reset when user wins or loses?
WordBank = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]     # List that contains all words for game
word = random.choice(WordBank)                      # Chooses a random word from word bank

print("Welcome to Hang Man")
print("Guess each letter of the word I'm thinking of.")


def compare(letter, chosen):                 # Compares letter to the letters in chosen word if any match
    for x in range(0, len(chosen)):
        if letter == word[x]:
            print("You got it! \n")
            return True
        elif x == len(word):
            print("Incorrect! \n")
            return False


while True:                                         # Allows user input and gives results output
    print(word)                                     # Prints word for testing purposes only
    
    guess = input('Please guess a letter ')         # User guesses letter
    print(" ")                                      # Prints an extra line after the user guesses letter
    Attempts += 1
    getAnswer = compare(guess, word)
    print(getAnswer)
    print(str(Attempts) + " Attempts made.")
    if guess == word:                               # If the user guesses the chosen word correctly 
        print("You won! \n")
    if getAnswer == True:                           # If the user guess letter input is correct
        letters.append(guess)
        Attempts = 0
        print("Your guess {} was correct.".format(guess))
        print("Your guesses so far, " + str((", ".join(letters))
    if getAnswer == False:                          # If the letter guess letter input from user is incorrect
        print("Your tries left: " + str(Tries))
    if Attempts == 10:                              # If Attempts hit 10 then the game ends
        break
