import ctools
def main():
    raw_data = ctools.wopen("day2.d")
    each_round = [i.strip().split(" ") for i in raw_data.strip().split("\n")]
    print(each_round)
    strategy_key = {
                "A": "rock",
                "B": "paper",
                "C": "scissors",
                "X": "rock",
                "Y": "paper",
                "Z": "scissors"
            }
    choice_value = {
                "rock": 1,
                "paper": 2,
                "scissors": 3
            }
    total = 0
    for r in each_round:
        computer = strategy_key[r[0]]
        player = strategy_key[r[1]]
        if (computer == "rock" and player == "scissors") or (computer =="paper" and player == "rock") or (computer == "scissors" and player == "paper"):
            score = choice_value[player] + 0
        elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
            score = choice_value[player] + 6
        else:
            score = choice_value[player] + 3
        total += score
    # part 1
    print(total)
    # part 2
    total = 0
    ultra_key = {
                "X":"lose",
                "Y":"draw",
                "Z":"win"
            }
    lose = {
                "rock": "paper",
                "paper": "scissors",
                "scissors": "rock"
            }
    win = {
                "rock": "scissors",
                "paper": "rock",
                "scissors": "paper"
            }
    for r in each_round:
        computer = strategy_key[r[0]]
        player = ultra_key[r[1]]
        if player == "lose":
            player = win[computer]
        elif player == "win":
            player = lose[computer]
        else:
            player = computer
        if (computer == "rock" and player == "scissors") or (computer =="paper" and player == "rock") or (computer == "scissors" and player == "paper"):
            score = choice_value[player] + 0
        elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
            score = choice_value[player] + 6
        else:
            score = choice_value[player] + 3
        total += score
    print(total)
    print("Success")


if __name__ == '__main__':
    main()
