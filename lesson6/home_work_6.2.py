while True:
    _number = int(input("Enter a number: "))
    days = _number // 86400
    hours = _number // 3600 % 24
    minutes = _number // 60 % 60
    seconds = _number % 60

    if days % 10 > 1 or not days % 10:
        days = f"{days} days"
    else:
        days = f"{days} day"

    if hours // 10 <= 1 and minutes // 10 <= 1 and seconds // 10 <= 1:
        print(days, f", 0{hours}:0{minutes}:0{seconds}")
    elif minutes // 10 <= 1 and seconds // 10 <= 1:
        print(days, f", {hours}:0{minutes}:0{seconds}")
    elif seconds // 10 <= 1:
        print(days, f", {hours}:{minutes}:0{seconds}")
    else:
        print(days, f", {hours}:{minutes}:{seconds}")

    the_end = input("\nType y to continue or any character to exit: ")
    if the_end != "Y" and the_end != "y":
        break
