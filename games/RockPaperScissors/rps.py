import random, sys, os, time 
"""
The Rock Paper Scissors format.
1. Should there be multiplayer gameplay? NAH
2. Should there be difficulties? NAH
3. Should there be a set format which can be applied to all langauges? YEAH
"""
winning_chart = {"rock":"scissors", "paper":"rock", "scissors":"paper"}

class Player:
    def __init__(self, health, name="default"):
        self.health = health
        self.name = name

def clear():
    os.system("clear")

def title_screen:
    clear()
    print("ROCK PAPER SCISSORS\nMade in Python")
    input("\nPress Enter to Start Playing...")
    clear()
    time.sleep(random.randint(1,2))

def instructionz():
   print("\nIn order to play you must type out your answer then hit enter.")
   print("\nYou can type and enter the following choices to choose your move...")
   print("Rock:       (R)ock,     r, 1")
   print("Paper:      (P)aper,    p, 2")
   print("Scissors:   (S)cissors, s, 3")
   print("\nYou only have 3 lives, good luck...")

def choice(inp):
    if inp in ["rock", "1"] or inp in "rock":
        return "rock"
    elif inp in ["paper", "2"] or inp in "paper":
        return "paper"
    elif inp in ["scissors", "3"] or inp in "scissors":
        return "scissors"
    else:
        print("Invalid move")

def save_winner(name):
    with open("leaderboard", "r") as f:
        Players = {}
        players_and_scores = f.read().strip().split("\n")
        for player_and_score in players_and_scores:
            player, score = player_and_score.split(" ")
            Players[player] = score
    if name in Players.keys():
        Players[name] = str(int(Players[name]) + 1)
    else:
        Players[name] = "1"
    with open("leaderboard", "w") as f:
        s = ""
        for key in Players.keys():
            s += f"{key} {Players[key]}\n"
        f.write(s)

def display_leaderboards():
    with open("leaderboard", "r") as f:
        Players = {}
        players_and_scores = f.read().strip().split("\n")
        for player_and_score in players_and_scores:
            player, score = player_and_score.split(" ")
            print(player + ": " + score) 

def decide_winner(player2, player1):
    # print(choice)
    if player2 == player1:
        return 0
    elif winning_chart[player2] == player1:
        return -1
    else:
        return 1

def instructions():
    print("Choose Rock, Paper, or Scissors")
    print("\nEither type it fully or use shorthand")
    print("(R)ock, r, 1\n(P)aper, p, 2\n(S)cissors, s, 3\n")

def main(comp=True):
    print("Rock Paper Scissors...")
    print("Press 'Enter' to Play")
    print("Press 'crtl+c' to quit")
    #if input() == "q":
    #    return 1
    player1 = Player(3, "Cody")
    player2 = Player(3, "Bum")
    for _ in range(100):
        os.system("clear")
        print(f"\nYOUR HEALTH\nYou: {player1.health}\nthem: {player2.health}\n")
        instructions()
        player1_move = choice(input("Your Move: ").lower())
        if comp:
            player2_move = choice(str(random.randint(1,3)))
        else:
            # gameplay isn't worked out.
            player2_move = choice(input("Your Move: ").lower())
        if player1_move in winning_chart.keys():
            decision = decide_winner(player2_move, player1_move)
            os.system("clear")
            print(f"\nYou Chose: {player1_move}\nThey chose: {player2_move}")
            time.sleep(random.randint(1,2))
            if decision == 1:
                print("\nYou Won")
                player2.health -= 1
            elif decision == 0:
                print("\nYou tied...")
            else:
                print("\nYou lost")
                player1.health -= 1
            time.sleep(random.randint(2,3))
        else:
            os.system("clear")
            print("\ntry again...")
            time.sleep(random.randint(1,2))

        if player1.health == 0:
            os.system("clear")
            print("You were beaten...")
            save_winner(player2.name)
            break
        elif player2.health == 0:
            os.system("clear")
            print(f"You beat {player2.name}...")
            save_winner(player1.name)
            break
    display_leaderboards()


main()
