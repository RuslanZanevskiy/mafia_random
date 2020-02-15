import random

try:
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
		if role == "житель":
			num = 0
			for r in roles.keys():
				num += roles[r]
			num = peoples - num
			print("Сколько \"{0}\" в игре: {1}".format(role, num))
			roles[role] = num
		else:
			roles[role] = int(input("Сколько \"{0}\" в игре: ".format(role)))
	  
	    	
	    
	print()
	
	for role in roles.keys():
	    chance = roles[role] / peoples * 100
	    print("Шанс что вы будете \"{0}\" - {1}%".format(role, chance))
except KeyboardInterrupt:
	print()
	print("Выход из программы...")
except ValueError:
	print()
	print("Ошибка значения, вводите коректные данные!")
	print("Выход из программы...")
except Exception as ex:
	print()
	print("Ошибка \"{0}\"".format(str(ex)))
	print("Выход из программы...")