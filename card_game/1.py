import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 1280, 1024
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Карточная игра Дурак")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Загрузка изображений карт
card_images = []
for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
    for rank in range(6, 11):
        image = pygame.image.load(f"img/cards/{suit}_{rank}.png")
        card_images.append({'image': image, 'suit': suit, 'rank': rank})
for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
    for rank in ['jack', 'queen', 'king', 'ace']:# Валет(11), Дама(12), Король(13), Туз(14)
        image = pygame.image.load(f"img/cards/{suit}_{rank}.png")
        card_images.append({'image': image, 'suit': suit, 'rank': rank})


# Создание колоды карт
deck = card_images
random.shuffle(deck)

# Раздача карт игрокам
player_hand = deck[:6]
computer_hand = deck[6:12]
table = deck[12:13]
taken_cards = []

# Функция проверки победителя
def check_winner(player_hand, computer_hand):
    if len(player_hand) == 0 or len(computer_hand) == 0:
        return 'player' if len(computer_hand) == 0 else 'computer'
    return None

# Главный игровой цикл
player_turn = True
run = True


card_width = 100
card_height = 160

player1_area = pygame.Rect(50, 50, 700, 200)
player2_area = pygame.Rect(50, 350, 700, 200)

player1_card_slots = [pygame.Rect(player1_area.left + i * 140 + 20, player1_area.top + 20, card_width, card_height) for
                      i in range(5)]
player2_card_slots = [pygame.Rect(player2_area.left + i * 140 + 20, player2_area.top + 20, card_width, card_height) for
                      i in range(5)]

player1_hand = random.sample(card_images, 5)
player2_hand = random.sample(card_images, 5)

while run:
    win.fill(WHITE)

    pygame.draw.rect(win, RED, player1_area, 2)

    for i, slot in enumerate(player1_card_slots):
        card_image = player1_hand[i]

        if not isinstance(card_image, pygame.surface.Surface):
            card_image = card_image.convert()
        win.blit(card_image, slot)

    pygame.draw.rect(win, RED, player2_area, 2)

    # for i, slot in enumerate(player2_card_slots):
    #     card_image = player2_hand[i]
    #
    #     if not isinstance(card_image, pygame.surface.Surface):
    #         card_image = card_image.convert()
    #     win.blit(card_image, slot)



    pygame.display.flip()

    # Отрисовка карт на экране
    # for i, card in enumerate(player_hand):
    #     win.blit(card['image'], ((5 + i * 150)/2, 275))
    # pygame.display.update()




    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Логика хода игроков
    winner = check_winner(player_hand, computer_hand)
    if winner:
        print(f"{winner.capitalize()} wins!")
        run = False
    else:
        if player_turn:
            # Ход игрока
            # Добавить здесь код для хода игрока
            player_turn = False
        else:
            # Ход компьютера
            # Добавить здесь код для хода компьютера
            player_turn = True

# Завершение игры
pygame.quit()