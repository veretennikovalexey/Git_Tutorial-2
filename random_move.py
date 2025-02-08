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

random_white = random.choice(white)
random_black = random.choice(black)

print(random_white)
print(random_black)