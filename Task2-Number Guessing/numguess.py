import random

def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Welcome to the Number Guessing Game!")
    upper_limit, lower_limit = input("Enter the range to guess the number from (format: upper_limit lower_limit): ").split()
    upper_limit = int(upper_limit)
    lower_limit = int(lower_limit)
    
    # Ensure lower_limit is less than or equal to upper_limit
    if lower_limit > upper_limit:
        lower_limit, upper_limit = upper_limit, lower_limit # Swap the values
    
    attempts = 0
    max_attempts = 5 # Maximum number of attempts allowed

    random_number = random.randint(lower_limit, upper_limit)

    while attempts < max_attempts:
        guess = get_valid_integer_input("Guess a number: ")

        if guess < random_number:
            print("Your guess is too low.")
        elif guess > random_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed it right! The number was {random_number}.")
            break
        
        attempts += 1
        print(f"You have {max_attempts - attempts} attempts left.")
    
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {random_number}.")

if __name__ == "__main__":
    main()
