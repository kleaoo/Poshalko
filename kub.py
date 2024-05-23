import random
from PIL import Image

def kubik():
    kubiki = int(input("количество куюиков которое вы хотите бросить: "))
    rolls = []

    for _ in range(kubiki):
        roll = random.randint(1, 6)
        rolls.append(roll)

    if kubiki == int('1488'):
        print ('посхалочка')
    elif kubiki == int('52'):
        print('пиписят тваа')
    elif kubiki == int('0'):
        im = Image.open('sigma.png')
        im.show()
    else:
        print("результат:", rolls)


kubik()