import random
import pygame

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 1200
screen_height = 800

# Создание экрана Pygame
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Игра в Дурака")

# Загрузка изображений карт
card_images = {}
suits = ['chervi', 'bubni', 'kresti', 'piki']
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

for suit in suits:
    card_images[suit] = {}
    for rank in ranks:
        card_images[suit][rank] = pygame.transform.scale(pygame.image.load(f'old/card/{suit}_{rank}.jpg'), (60, 90))

# Определение размеров карты
card_width = card_images['chervi']['6'].get_width()
card_height = card_images['chervi']['6'].get_height()

# Создание руки игрока
player_hand = []

# Создание руки противника
enemy_hand = []

# Создание колоды
deck = [(suit, rank) for suit in suits for rank in ranks]
random.shuffle(deck)

# Раздача карт игрокам
player_hand = deck[:6]
enemy_hand = deck[:6]
deck = deck[6:]

# Переменная, чтобы хранить текущую активную карту
active_card = None

# Флаги для управления ходом игры
is_selecting_card = False
is_discarding_card = False

# Основной цикл игры
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not is_selecting_card and not is_discarding_card:
                # Игрок выбирает карту
                mouse_pos = pygame.mouse.get_pos()
                for i, (_suit, _rank) in enumerate(player_hand):
                    card_x = 50 + i * (card_width + 10)
                    card_y = 50
                    if card_x <= mouse_pos[0] <= card_x + card_width and card_y <= mouse_pos[1] <= card_y + card_height:
                        active_card = player_hand[i]
                        is_selecting_card = True
                        break
            elif is_selecting_card and not is_discarding_card:
                # Игрок сбрасывает карту
                mouse_pos = pygame.mouse.get_pos()
                if screen_width / 2 - card_width / 2 <= mouse_pos[0] <= screen_width / 2 + card_width / 2 and screen_height / 2 - card_height / 2 <= mouse_pos[1] <= screen_height / 2 + card_height / 2:
                    # Карта сброшена
                    player_hand.remove(active_card)
                    active_card = None
                    is_selecting_card = False
                    is_discarding_card = True

    # Отрисовка состояния игры
    screen.fill((0, 128, 0))  # Зеленый фон

    # Отрисовка карт в руке игрока
    def draw_player_hand(screen, player_hand):
        for i, (suit, rank) in enumerate(player_hand):
            card_x = 50 + i * (card_width + 10)
            card_y = 50
            screen.blit(card_images[suit][rank], (card_x, card_y))

    # Отрисовка карт противника
    def draw_enemy_hand(screen, enemy_hand):
        for i in range(len(enemy_hand)):
            card_back_image = pygame.transform.scale(pygame.image.load('old/card/d04605r001c.jpg'), (60, 90))
            card_x = 50 + i * (card_width + 10)
            card_y = 50
            screen.blit(card_back_image, (card_x, card_y))


    # Отрисовка карт игрока
    draw_player_hand(screen, player_hand)

    # Отрисовка обложек карт противника
    draw_enemy_hand(screen, enemy_hand)

    # Отрисовка активной карты (если есть)
    if active_card:
        screen.blit(card_images[active_card[0]][active_card[1]], (screen_width // 2 - card_width // 2, screen_height // 2 - card_height // 2))

    pygame.display.flip()

# Завершение игры
pygame.quit()