import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Карточная игра Дурак")

# Цвета
WHITE = (255, 255, 255)

# Загрузка изображений карт
card_images = []
for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
    for rank in range(6, 15):  # Валет(11), Дама(12), Король(13), Туз(14)
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
while run:
    win.fill(WHITE)
    
    # Отрисовка карт на экране
    for i, card in enumerate(player_hand):
        win.blit(card['image'], (50 + i * 100, 400))
        
    pygame.display.update()
    
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
            # Добавьте здесь код для хода игрока
            player_turn = False
        else:
            # Ход компьютера
            # Добавьте здесь код для хода компьютера
            player_turn = True

# Завершение игры
pygame.quit()