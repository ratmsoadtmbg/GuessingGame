import random

def save_high_score(score, filename="highscore.txt"):
    try:
        with open(filename, "w") as f:
            f.write(str(score))
    except IOError:
        print("Error: Unable to save high score.")

def load_high_score(filename="highscore.txt"):
    try:
        with open(filename, "r") as f:
            high_score = int(f.read())
            return high_score
    except (FileNotFoundError, ValueError):
        return 0  # Returns 0 if file doesn't exist or content is invalid

def main():
    number = random.randint(1,9)
    guessed = False
    guesses = []
    guess_limit = 5 # Change number of guesses allowed here
    high_score = load_high_score()

    print(f"I'm thinking of a number between 0 and 10. Can you guess it in {guess_limit} tries?\nThe current lowest guess score is {high_score}.\n")
    
    while guessed == False and guess_limit != 0:
        if guesses:
            print(guesses)
        try:
            guess = int(input("Type guess here: "))
        except ValueError:
            print("I know you think you're clever, but please try to stick to simple numbers here.\n")
            continue
        if guess < number:
            guess_limit -= 1
            print(f"\nToo low! You have {guess_limit} attempts left.")
            guesses.append(f">{guess}")
        elif guess > number:
            guess_limit -= 1
            print(f"\nToo high! You have {guess_limit} attempts left.")
            guesses.append(f"<{guess}")
        else:
            guessed = True
            
    score = len(guesses)+1
    
    if guessed == True:
        if not guesses:
            save_high_score(1)
            print(f"\nCongratulations! You guessed the number in 1 try!")
        else:
            if score < high_score:
                save_high_score(score)    
            print(f"\nCongratulations! You guessed the number in {score} tries!")
    else:
        print("You have run out of guesses!")
    
    play_again = input("\nWould you like to play again? (Y/N): ").lower()
    if play_again != "y" and play_again != "n":
        play_again = input('\nSorry but "Y" and "N" are your only options. Would you like to play again?: ') # Gives second chance to put a valid response
    if play_again != "y" and play_again != "n":
        print("\nOkay, wise guy, have it your way.") # Boots wiley players who won't respond properly
    if play_again == "y":
        main()
    if play_again == "n":
        print("Thanks for playing!")


main()

