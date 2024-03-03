# Работа с циклом while |

number = 97
running = True #Мы задаём значение True и цыкл понимает, что он может работать |

while running:
	guess = int(input("Угадай число: "))

	if guess == number:
		print("Ты угадал!")
		running = False #Останавливает цикл если задать значение False |
	elif guess > number:
		print("Угаданное число больше чем загаданое.")
	else:
		print("Угаданное число меньше чем загаданое.")
else:
	print("Цыкл while завершён.") #Он останавливаеться если значение переменной running == False