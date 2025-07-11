import random

def main():
    number = random.randint(0,10)
    guessed = False
    guesses = []

    print("I'm thinking of a number between 0 and 10. Can you guess it?\n")
    
    while guessed == False:
        if guesses:
            print(guesses)
        try:
            guess = int(input("Type guess here: "))
        except:
            raise Exception("I know you think you're clever, but please try to stick to simple numbers here.")
        if guess < number:
            print("\nToo low! Try again!")
            guesses.append(f">{guess}")
            continue
        if guess > number:
            print("\nToo high! Try again!")
            guesses.append(f"<{guess}")
            continue
        else:
            guessed = True
    
    if not guesses:
        print(f"\nCongratulations! You guessed the number in 1 try! See you next time!")
    else:    
        print(f"\nCongratulations! You guessed the number in {len(guesses)+1} tries! See you next time!")


main()