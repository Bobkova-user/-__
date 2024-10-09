hour = int(input("Введите время в часах (0-23): "))

if (hour < 8) or (hour >= 22) or (10 <= hour < 12) or (14 <= hour < 15) or (18 <= hour < 20):
    print("Посылку получить нельзя.")
else:
    print("Можно получить посылку.")