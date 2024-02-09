import random
import pygame

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 800
screen_height = 600

# Создание экрана Pygame
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Игра в Дурака")

# Загрузка изображений карт
card_images = {
    'черви': {
        '6': pygame.image.load('card/chervi_6.jpg'),
        '7': pygame.image.load('card/chervi_7.jpg'),
        '8': pygame.image.load('card/chervi_8.jpg'),
        '9': pygame.image.load('card/chervi_9.jpg'),
        '10': pygame.image.load('card/chervi_10.jpg'),
        'валет': pygame.image.load('card/chervi_J.jpg'),
        'дама': pygame.image.load('card/chervi_Q.jpg'),
        'король': pygame.image.load('card/chervi_K.jpg'),
        'туз': pygame.image.load('card/chervi_A.jpg')
    },
    'бубны': {
        '6': pygame.image.load('card/bubni_6.jpg'),
        '7': pygame.image.load('card/bubni_7.jpg'),
        '8': pygame.image.load('card/bubni_8.jpg'),
        '9': pygame.image.load('card/bubni_9.jpg'),
        '10': pygame.image.load('card/bubni_10.jpg'),
        'валет': pygame.image.load('card/bubni_J.jpg'),
        'дама': pygame.image.load('card/bubni_Q.jpg'),
        'король': pygame.image.load('card/bubni_K.jpg'),
        'туз': pygame.image.load('card/bubni_A.jpg')
    },
    'крести': {
        '6': pygame.image.load('card/kresti_6.jpg'),
        '7': pygame.image.load('card/kresti_7.jpg'),
        '8': pygame.image.load('card/kresti_8.jpg'),
        '9': pygame.image.load('card/kresti_9.jpg'),
        '10': pygame.image.load('card/kresti_10.jpg'),
        'валет': pygame.image.load('card/kresti_J.jpg'),
        'дама': pygame.image.load('card/kresti_Q.jpg'),
        'король': pygame.image.load('card/kresti_K.jpg'),
        'туз': pygame.image.load('card/kresti_A.jpg')
    },
    'пики': {
    '6': pygame.image.load('card/piki_6.jpg'),
    '7': pygame.image.load('card/piki_7.jpg'),
    '8': pygame.image.load('card/piki_8.jpg'),
    '9': pygame.image.load('card/piki_9.jpg'),
    '10': pygame.image.load('card/piki_10.jpg'),
    'валет': pygame.image.load('card/piki_J.jpg'),
    'дама': pygame.image.load('card/piki_Q.jpg'),
    'король': pygame.image.load('card/piki_K.jpg'),
    'туз': pygame.image.load('card/piki_A.jpg')
    }
}

# Определение размеров карты
card_width = card_images['черви']['6'].get_width()
card_height = card_images['черви']['6'].get_height()

# Создание руки игрока
player_hand = []

# Создание колоды
deck = []
suits = ['черви', 'бубны', 'крести', 'пики']
ranks = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
for suit in suits:
    for rank in ranks:
        deck.append((suit, rank))

# Перетасовка колоды
random.shuffle(deck)

# Раздача карт игроку
for _ in range(6):
    player_hand.append(deck.pop())

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
                for i in range(len(player_hand)):
                    card_x = 50 + i * (card_width + 10)
                    card_y = screen_height - card_height - 50
                    if card_x <= mouse_pos[0] <= card_x + card_width and \
                        card_y <= mouse_pos[1] <= card_y + card_height:
                        active_card = player_hand[i]
                        is_selecting_card = True
                        break
            elif is_selecting_card and not is_discarding_card:
                # Игрок сбрасывает карту
                mouse_pos = pygame.mouse.get_pos()
                if screen_width / 2 - card_width / 2 <= mouse_pos[0] <= screen_width / 2 + card_width / 2 and \
                    screen_height / 2 - card_height / 2 <= mouse_pos[1] <= screen_height / 2 + card_height / 2:
                    # Карта сброшена
                    player_hand.remove(active_card)
                    active_card = None
                    is_selecting_card = False
                    is_discarding_card = True

    # Отрисовка состояния игры
    screen.fill((0, 128, 0)) # Зеленый фон

    # Отрисовка карт в руке игрока
    for i, (suit, rank) in enumerate(player_hand):
        card_x = 50 + i * (card_width + 10)
        card_y = screen_height - card_height - 50
        screen.blit(card_images[suit][rank], (card_x, card_y))

    # Отрисовка активной карты (если есть)
    if active_card:
        screen.blit(card_images[active_card[0]][active_card[1]], (screen_width / 2 - card_width / 2,
        screen_height / 2 - card_height / 2))

    pygame.display.flip()

# Завершение игры
pygame.quit()