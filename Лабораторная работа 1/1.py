numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers[4] = 0  #заменил None на о
# TODO заменить значение пропущенного элемента средним арифметическим
Overall = sum(numbers)  #нашел сумму всех чисел
Onerall = len(numbers)  #нашел колличество цифр
Arifmet = Overall / (Onerall)  # нашел среднее арифметическое
numbers[4] = Arifmet
print("Измененный список:", numbers)