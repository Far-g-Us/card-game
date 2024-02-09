import random

num_players = 2 # указываем количество игроков

# Создаем колоду карт
suits = ['черви', 'бубны', 'крести', 'пики'] # масти
ranks = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'] # достоинства

if num_players == 2:
    ranks.extend(['туз'])
    num_cards = 36
elif num_players == 4:
    ranks.extend(['туз']*2 + ['2', '3', '4', '5'])
    num_cards = 54

deck = [(suit, rank) for suit in suits for rank in ranks] # создаем колоду из всех комбинаций мастей и достоинств
random.shuffle(deck)

# Определяем козырную масть
trump_suit = random.choice(suits)

# Раздаем карты игрокам
player_hands = [[] for _ in range(num_players)] # список для хранения рук каждого игрока

for _ in range(6): # раздаем по 6 карт каждому игроку
    for i in range(num_players):
        player_hands[i].append(deck.pop())

# Определение игрока, который начинает ход
starting_player = None

for i in range(num_players):
    if any(card[0] == trump_suit for card in player_hands[i]):
        starting_player = i
        break

if starting_player is None:
    starting_player = random.randint(0, num_players - 1)

# Бита
bita = []

# игровой цикл
current_player = starting_player

while all(len(hand) > 1 for hand in player_hands):
    # Выводим карты на руках
    print("Ваша козырная масть:", trump_suit)

    for i in range(num_players):
        print(f"Карты игрока {i+1}:", [card[1] + " " + card[0] for card in player_hands[i]])

    # Ход игрока
    if current_player == 0:
        player_card_index = int(input("Выберите индекс карты для хода: "))
        player_card = player_hands[current_player].pop(player_card_index)
    else:
        player_card = random.choice(player_hands[current_player])
        player_hands[current_player].remove(player_card)

    # Ход компьютеров
    if current_player == 0:
        computer_card = random.choice(player_hands[1])
        player_hands[1].remove(computer_card)
    else:
        computer_card = random.choice(player_hands[0])
        player_hands[0].remove(computer_card)

    # Выводим карты, которыми ходили игроки
    print(f"{'Вы' if current_player == 0 else f'Компьютер {current_player}'} сыграли карту: {player_card[1]} {player_card[0]}")
    print(f"{'Компьютер {current_player}' if current_player == 0 else 'Вы'} сыграли карту: {computer_card[1]} {computer_card[0]}")

    # Вычисляем, кто победил в этом раунде
    if player_card[0] == trump_suit and computer_card[0] != trump_suit:
        print("Вы выиграли раунд!")
        player_hands[current_player].append(player_card)
    elif player_card[0] != trump_suit and computer_card[0] == trump_suit:
        print("Компьютер выиграл раунд!")
        player_hands[current_player].append(computer_card)
    elif suits.index(player_card[0]) > suits.index(computer_card[0]):
        print("Вы выиграли раунд!")
        player_hands[current_player].append(player_card)
    else:
        print("Компьютер выиграл раунд!")
        player_hands[current_player].append(computer_card)

    # Если игрок побил все карты
    if len(player_hands[current_player]) == 0:
        print("Вы отбились!")
        bita.extend([player_card, computer_card])
    else:
        print(f"Компьютер отбился!")
        bita.extend([player_card, computer_card])

    # Печатаем кол-во оставшихся карт
    for i in range(num_players):
        print(f"У игрока {i+1} осталось", len(player_hands[i]), "карт.")

    print()

    # Изменяем игрока, который будет ходить в следующем раунде
    current_player = (current_player + 1) % num_players

# Взять недостающие карты в конце хода
for i in range(num_players):
    player_hands[i].extend(deck[:6 - len(player_hands[i])])

# Определение победителя
winners = []
for i in range(num_players):
    if len(player_hands[i]) <= 1:
        winners.append(str(i+1))

if len(winners) > 1:
    print("Победители:", ", ".join(winners))
else:
    print(f"Игрок {winners[0]} победил!")