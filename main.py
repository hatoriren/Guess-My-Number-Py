import random

print("\tWelcome to Guess My Number")

def play_game():
    random_number = random.randint(1, 100)
    count = 0

    while True:
        if count > 0 and count % 5 == 0:
            hint = input("Do you want a hint? (yes/no): ").lower().strip()
            if hint == "yes":
                lower_bound = max(0, random_number - random.randint(1, 10))
                upper_bound = min(random_number + random.randint(1, 10), 100)
                print(f"Your number is in the range of {lower_bound} to {upper_bound}")
        while True:
            try:
                user_number = int(input("Write a number (from 1 to 100): "))
                break
            except ValueError:
                print("It`s not a number. ")
        count += 1

        if user_number < random_number:
            if random_number - user_number > 10:
                print("Too low")
            else:
                print("Low, but you're close")

        elif user_number > random_number:
            if user_number - random_number > 10:
                print("Too high")
            else:
                print("High, but you're close")

        else:
            print(f"\tThat's it! You got {count} tries!")
            break

while True:
    play_game()
    end_game = input("\tDo you want to play again? (yes/no): ").lower().strip()
    if end_game != "yes":
        break
