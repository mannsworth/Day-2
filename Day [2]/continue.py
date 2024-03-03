while True:
	s = input("Введите строку: ")
	if s == "выход":
		break
	if len(s) < 3:
		print("Строка слишком маленькая")
		continue
	print("Строка достаточной длины")