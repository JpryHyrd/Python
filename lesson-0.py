import random
words = ["элипсоид", "плоскость"]
name = input("Введите свое имя: ")
print("Здравствуйте", name + "!")
slovo = random.choice(words)
print("Вам загадано слово, попробуйте его отгадать!\nЕсли понадобится подсказка - нажмите 1")
print("Для выхода нажмите 2")
while True:
	if slovo == words[0]:
		answer = input("\t\tФорма земли - 8 букв: \n\t")
		answer = answer.lower()
		if answer == "1":
			print("\t\tПервая буква -", slovo[0])
		elif answer == slovo:
			print("\t\tВы угадали!")
			break
		elif answer == "2":
			print("\t\t\tДо свидания!")
			break
		else:
			print("\t\t\tНеверный ответ, попробуйте еще раз!")
	elif slovo == words[1]:
		answer = input("\t\tЧто можно провести через 3 точки, причем только одну - 9 букв:\n\t")
		answer = answer.lower()
		if answer == "1":
			print("\t\tПервая буква -", slovo[0])
		elif answer == slovo:
			print("\t\t\tВы угадали!")
			break
		elif answer == "2":
			print("\t\t\tДо свидания!")
			break
		else:
			print("\t\t\tНеверный ответ, попробуйте еще раз!")
