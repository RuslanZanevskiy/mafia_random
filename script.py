import random

peoples = int(input("Введите количество людей: "))

print()

roles = {
    "мафия":0,
    "доктор":0,
    "комисар":0,
    "маньяк":0,
    "житель":0
}

for role in roles.keys():
    roles[role] = int(input("Сколько \"{0}\" в игре: ".format(role)))
    
print()

for role in roles.keys():
    chance = roles[role] / peoples * 100
    print("Шанс что вы будете \"{0}\" - {1}%".format(role, chance))
