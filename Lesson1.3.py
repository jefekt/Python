num = list(range(0, 21))

for num in range(0, 21):
    if num == 0:
        print(f"{num}  Процентов")
    if num == 1:
        print(f"{num}  Процент")
    if 1 < num < 5:
        print(f"{num}  Процента")
    if 0 <= num <= 20 and 5 <= num <= 20:
        print(f"{num}  Процентов")
