_number = int(input("Введіть ціле 5-х значне число\n"))
return_number = _number % 10 * 10000 + _number % 100 // 10 * 1000 + _number // 100 % 10 * 100 + _number // 1000 % 10 * 10 + _number // 10000
print(return_number)
