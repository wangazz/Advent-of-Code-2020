import os
input_path = '../Inputs/Day-22.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

def score(cards):
    scores = [(len(cards) - i) * card for i, card in enumerate(cards)]
    return sum(scores)

# Part 1
player_1 = []
player_2 = []

current_player = 0
for line in inputs:
    if line == 'Player 1:':
        current_player = 1
    elif line == 'Player 2:':
        current_player = 2
    elif line == '':
        pass
    elif current_player == 1:
        player_1.append(int(line))
    elif current_player == 2:
        player_2.append(int(line))

while len(player_1) != 0 and len(player_2) != 0:
    card_1 = player_1[0]
    card_2 = player_2[0]
    if card_1 > card_2:
        player_1 += [max(card_1, card_2), min(card_1, card_2)]
    else:
        player_2 += [max(card_1, card_2), min(card_1, card_2)]
    player_1.pop(0)
    player_2.pop(0)

winner = player_1 if len(player_2) == 0 else player_2
print(score(winner))

# Part 2
player_1 = []
player_2 = []

current_player = 0
for line in inputs:
    if line == 'Player 1:':
        current_player = 1
    elif line == 'Player 2:':
        current_player = 2
    elif line == '':
        pass
    elif current_player == 1:
        player_1.append(int(line))
    elif current_player == 2:
        player_2.append(int(line))

def game(player_1, player_2):
    history = []
    winner = int()

    while len(player_1) != 0 and len(player_2) != 0:
        if (player_1, player_2) in history:
            winner = 1
            break

        card_1 = player_1[0]
        card_2 = player_2[0]
        history.append((player_1.copy(), player_2.copy()))

        if len(player_1) > card_1 and len(player_2) > card_2:
            new_player_1, new_player_2 = player_1[1:card_1 + 1], player_2[1:card_2 + 1]
            winner = game(new_player_1, new_player_2)[0]
        else:
            winner = 1 if card_1 > card_2 else 2

        if winner == 1:
            player_1 += [card_1, card_2]
        else:
            player_2 += [card_2, card_1]

        player_1.pop(0)
        player_2.pop(0)

    return (1, player_1) if len(player_1) != 0 else (2, player_2)

winner, winning_hand = game(player_1, player_2)
print(score(winning_hand))
