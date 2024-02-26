import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH = 800
HEIGHT = 600

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создание игрового окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Дурак")

# Загрузка изображений карт
card_images = []
for suit in ["hearts", "diamonds", "clubs", "spades"]:
    for value in range(6, 15):
        image = pygame.image.load(f"cards/{suit}_{value}.png")
        card_images.append(image)

# Класс для представления карты
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = card_images[(suit - 1) * 7 + (value - 6)]

# Класс для представления колоды карт
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(1, 5):
            for value in range(6, 15):
                card = Card(suit, value)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

# Класс для представления игрока
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self, card_index):
        return self.hand.pop(card_index)

# Функция для игры
def play_game():
    # Создание игроков
    player1 = Player("Игрок 1")
    player2 = Player("Игрок 2")
    player3 = Player("Игрок 3")
    player4 = Player("Игрок 4")

    # Создание колоды карт и ее перемешивание
    deck = Deck()
    deck.shuffle()

    # Раздача карт игрокам
    for _ in range(6):
        player1.add_card(deck.draw())
        player2.add_card(deck.draw())
        player3.add_card(deck.draw())
        player4.add_card(deck.draw())

    # Основной игровой цикл
    while len(player1.hand) > 0 and len(player2.hand) > 0 and len(player3.hand) > 0 and len(player4.hand) > 0:
        # Ход игрока 1
        card_index = random.randint(0, len(player1.hand) - 1)
        played_card1 = player1.play_card(card_index)

        # Ход игрока 2
        card_index = random.randint(0, len(player2.hand) - 1)
        played_card2 = player2.play_card(card_index)

        # Ход игрока 3
        card_index = random.randint(0, len(player3.hand) - 1)
        played_card3 = player3.play_card(card_index)

        # Ход игрока 4
        card_index = random.randint(0, len(player4.hand) - 1)
        played_card4 = player4.play_card(card_index)

        # Вывод ходов игроков на консоль
        print(f"{player1.name} сыграл карту {played_card1.value} {played_card1.suit}")
        print(f"{player2.name} сыграл карту {played_card2.value} {played_card2.suit}")
        print(f"{player3.name} сыграл карту {played_card3.value} {played_card3.suit}")
        print(f"{player4.name} сыграл карту {played_card4.value} {played_card4.suit}")

        # Проверка на выигрыш карты
        if played_card1.value > played_card2.value and played_card1.value > played_card3.value and played_card1.value > played_card4.value:
            print(f"{player1.name} выиграл!")
        elif played_card2.value > played_card1.value and played_card2.value > played_card3.value and played_card2.value > played_card4.value:
            print(f"{player2.name} выиграл!")
        elif played_card3.value > played_card1.value and played_card3.value > played_card2.value and played_card3.value > played_card4.value:
            print(f"{player3.name} выиграл!")
        elif played_card4.value > played_card1.value and played_card4.value > played_card2.value and played_card4.value > played_card3.value:
            print(f"{player4.name} выиграл!")
        else:
            print("Ничья!")

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Заполнение фона
    screen.fill(WHITE)

    # Отображение карт игроков на экране
    for i, card_image in enumerate(card_images):
        x = (i % 6) * 100 + 50
        y = (i // 6) * 150 + 50
        screen.blit(card_image, (x, y))

    for j, card_image in enumerate(card_images):
        x = (j % 6) * 100 + 50
        y = (j // 6) * 150 + 400
        screen.blit(card_image, (x, y))

    # Обновление экрана
    pygame.display.flip()

# Запуск игры
play_game()

# Выход из игры
pygame.quit()