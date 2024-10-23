price_chair_1 = float(input("Введите стоимость первого стула (в рублях): "))
price_chair_2 = float(input("Введите стоимость второго стула (в рублях): "))
price_chair_3 = float(input("Введите стоимость третьего стула (в рублях): "))

total_price = price_chair_1 + price_chair_2 + price_chair_3

if total_price > 10000:
    discount = total_price * 0.10 
    total_price -= discount  
print(f"Итоговая сумма чека составляет: {total_price:.2f} рублей.")