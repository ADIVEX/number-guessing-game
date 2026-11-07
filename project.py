import random
decision = "yes"
while decision == "yes":
    target = random.randint(1,100)
    for i in range(1,6):
        n = int(input("Enter a number between 1-100 "))
        if n > 100:
            print("Range is between 1-100 plz enter the number range within")
            break
        if target == n and i == 1:
            print("Congratulations! You guessed it in 1 attempt")
            break
        if target == n and i != 1:
            print("Congratulations! You guessed it in ",i," attempt")
            break
        else:
            if target < n:
                print('''Too High!
        Attempts left: ''',(5-i))
            else:
                print('''Too Low!
        Attempts left: ''',(5-i))
    if n != target and n < 100:
        print("Game Over! ")
        print(f"The number was {target}")
    print("Wants to paly again enter yes otherwise no ")
    decision = input().strip().lower()
if decision != "yes":
    print("Thank you! Come next time with better luck.")