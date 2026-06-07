import random

level = 1

while True:
    secret_number = random.randint(1, level * 10)

    print("\n🎮 Level", level)
    print("Guess a number between 1 and", level * 10)

    for chance in range(3):
        number = int(input("Enter your guess: "))

        if number == secret_number:
            print("🎉 Correct! Moving to the next level.")
            level += 1
            break

        else:
            print("❌ Wrong guess!")
            print("Chances left:", 2 - chance)

    else:
        print("\n💀 Game Over!")
        print("The secret number was:", secret_number)
        break