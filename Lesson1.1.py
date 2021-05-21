num = int(input("Enter your numbers: "))

d = num // 86400
h = num // 3600 % 24
m = num // 60 % 60
s = num % 60

print(f"{d} дней {h} час {m} мин {s} секунд")
