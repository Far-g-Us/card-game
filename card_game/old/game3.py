import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 1200
screen_height = 800

# Цвета
white = (255, 255, 255)
green = (0, 128, 0)

# Создание экрана Pygame
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Карточная игра 'Дурак'")

# Списки мастей и достоинств карт
suits = ['chervi', 'bubni', 'kresti', 'piki']
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Загрузка изображений карт с измененным размером
card_width = 60
card_height = 90

# Загрузка изображений карт
card_images = []
for suit in suits:
    for rank in ranks:
        card_img = pygame.image.load(f'old/card/{suit}_{rank}.jpg')
        scaled_card_img = pygame.transform.scale(card_img, (card_width, card_height))
        card_images.append(scaled_card_img)

# Создание колоды карт
deck = random.sample(card_images, 6)

# Расположение колод на экране
deck_positions = [(50, 320), (200, 320), (350, 320)]

# Основной цикл игры
running = True
selected_card = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, pos in enumerate(deck_positions):
                if pos[0] <= mouse_pos[0] <= pos[0] + card_images[0].get_width() and pos[1] <= mouse_pos[1] <= pos[1] + card_images[0].get_height():
                    if selected_card is None:
                        selected_card = deck[i]
                    else:
                        deck[i], deck[deck.index(selected_card)] = selected_card, deck[i]
                        selected_card = None

    # Отрисовка игрового состояния
    screen.fill(green)
    for i, card in enumerate(deck):
        if i < len(deck_positions):  # Проверка диапазона индекса
            screen.blit(card, deck_positions[i])
    if selected_card:
        screen.blit(selected_card, pygame.mouse.get_pos())

    pygame.display.flip()

# Завершение игры
pygame.quit()