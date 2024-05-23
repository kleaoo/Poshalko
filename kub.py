import random

def kubik():
    kubiki = int(input("количество куюиков которое вы хотите бросить: "))
    rolls = []

    for _ in range(kubiki):
        roll = random.randint(1, 6)
        rolls.append(roll)

    print("результат:", rolls)
kubik()