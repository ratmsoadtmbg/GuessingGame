import random

def main():
    number = random.randint(1,9)
    guessed = False
    guesses = []

    print("I'm thinking of a number between 0 and 10. Can you guess it?\n")
    
    while guessed == False:
        if guesses:
            print(guesses)
        try:
            guess = int(input("Type guess here: "))
        except ValueError:
            print("I know you think you're clever, but please try to stick to simple numbers here.\n")
            continue
        if guess < number:
            print("\nToo low! Try again!")
            guesses.append(f">{guess}")
        elif guess > number:
            print("\nToo high! Try again!")
            guesses.append(f"<{guess}")
        else:
            guessed = True
    
    if not guesses:
        print(f"\nCongratulations! You guessed the number in 1 try!")
    else:    
        print(f"\nCongratulations! You guessed the number in {len(guesses)+1} tries!")
    play_again = input("\nWould you like to play again? (Y/N): ").lower()
    if play_again != "y" and play_again != "n":
        play_again = input('\nSorry but "Y" and "N" are your only options. Would you like to play again?: ')
    if play_again != "y" and play_again != "n":
        print("\nOkay, wise guy, have it your way.")
    if play_again == "y":
        main()
    if play_again == "n":
        print("Thanks for playing!")


main()

