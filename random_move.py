import random

white = [
    "a4",
    "a3",
    "b4",
    "b3",
    "c4",
    "c3",
    "d4",
    "d3",
    "e4",
    "e3",
    "f4",
    "f3",
    "g4",
    "g3",
    "h4",
    "h3",
    "Na3",
    "Nc3",
    "Nf3",
    "Nh3",
]

black = [
    "a5",
    "a6",
    "b5",
    "b6",
    "c5",
    "c6",
    "d5",
    "d6",
    "e5",
    "e6",
    "f5",
    "f6",
    "g5",
    "g6",
    "h5",
    "h6",
    "Na6",
    "Nc6",
    "Nf6",
    "Nh6",
]

# Перемешиваем списки ходов
random.shuffle(white)
random.shuffle(black)

# Выбираем первый элемент из перемешанных списков
# Это эквивалентно случайному выбору, но с другим алгоритмом
random_white = white[0]
random_black = black[0]

# Альтернативный способ со случайным индексом
# Использование двух различных методов выбора повышает "случайность"
index_white = random.randint(0, len(white) - 1)
index_black = random.randint(0, len(black) - 1)
random_white_alt = white[index_white]
random_black_alt = black[index_black]

# Выбор метода с 50% вероятностью для каждого цвета
if random.random() < 0.5:
    final_white = random_white
else:
    final_white = random_white_alt

if random.random() < 0.5:
    final_black = random_black
else:
    final_black = random_black_alt

print(final_white)
print(final_black)