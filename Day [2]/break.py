# Работа с оператором цикла while -- break |

running = True

while running:
	string = input("Введите команду: ")
	if str(string) == "выход":
		print("Закрываю цикл...")
		break
	else:
		print("Длина строки: ", len(str(string)))