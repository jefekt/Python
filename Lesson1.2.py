def sum_digits(value):
    res = 0

    while value != 0:
        res += value % 10
        value //= 10

    return res


num = [i ** 3 for i in range(1, 1001, 2)]

res1 = sum(filter(lambda num: sum_digits(num) % 7 == 0, num))
res2 = sum(filter(lambda num: sum_digits(num + 17) % 7 == 0, num))

print(res1)
print(res2)
