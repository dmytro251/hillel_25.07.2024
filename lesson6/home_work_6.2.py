while True:
    _number = int(input("Вкажіть кількість секунд: "))
    days = _number // 86400
    hours = _number // 3600 % 24
    minutes = _number // 60 % 60
    seconds = _number % 60

    if 5 < days < 20 or not days % 10 or days % 10 in range(5, 10):
        print(f"{days} Днів {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
    elif days % 10 in range(2, 5):
        print(f"{days} Дні {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
    else:
        print(f"{days} День {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

    the_end = input("\nType y to continue or any character to exit: ")
    if the_end != "Y" and the_end != "y":
        break
