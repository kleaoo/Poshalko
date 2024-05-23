import random
from PIL import Image

def kubik():
    kubiki = int(input("количество куюиков которое вы хотите бросить: "))
    rolls = []

    for _ in range(kubiki):
        roll = random.randint(1, 6)
        rolls.append(roll)

    if kubiki == int('1488'):
        jo = Image.open('joker.jpg')
        jo.show()
    elif kubiki == int('52'):
        print('пиписят тваа')
    elif kubiki == int('0'):
        si = Image.open('sigma.jpg')
        si.show()
    elif kubiki == int('781'):
        print('опа сво')
    elif kubiki == int('1989'):
        hm = Image.open('hm.jpg')
        hm.show()
    else:
        print("результат:", rolls)
kubik()