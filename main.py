import random

print("WELCOME TO STONE PAPER SCISSOR GAME WITH YOUR PC")
print("Choose your move against your COMPUTER as 1, 2, or 3")
print("1. PAPER")
print("2. STONE")
print("3. SCISSOR")
print("0. TO EXIT AND SHOW SCORE")

# Score counters
wins = 0
losses = 0
draws = 0

while True:
    user_input = int(input("\nEnter your choice (1-Paper, 2-Stone, 3-Scissor, 0-Exit): "))

    if user_input == 0:
        print("\nGame Over!")
        print("Final Score:")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Draws: {draws}")
        if(wins>losses):
          print(f"YOU WON THE GAME AGAINST COMPUTER BY THE MARGIN OF {(wins-losses)}")
        elif(losses>wins):
          print(f"YOU LOST THE GAME AGAINST COMPUTER BY THE MARGIN OF {(losses-wins)}")
        else:
          print(f"YOU HAVE EQUAL SCORE")
        break

    if user_input > 3 or user_input < 0:
        print("Invalid choice! Please enter 1, 2, 3, or 0 to quit.")
        continue

    computer_move = random.randint(1, 3)

    if user_input == computer_move:
        print("DRAW")
        draws += 1
    elif user_input == 1 and computer_move == 2:
        print("Paper vs Stone")
        print("You WON the game")
        wins += 1
    elif user_input == 2 and computer_move == 1:
        print("Stone vs Paper")
        print("You LOST the game")
        losses += 1
    elif user_input == 3 and computer_move == 2:
        print("Scissor vs Stone")
        print("You LOST the game")
        losses += 1
    elif user_input == 2 and computer_move == 3:
        print("Stone vs Scissor")
        print("You WON the game")
        wins += 1
    elif user_input == 3 and computer_move == 1:
        print("Scissor vs Paper")
        print("You WON the game")
        wins += 1
    elif user_input == 1 and computer_move == 3:
        print("Paper vs Scissor")
        print("You LOST the game")
        losses += 1
