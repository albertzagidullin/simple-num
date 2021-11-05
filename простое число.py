# объявление функции
def get_next_prime(num):
    # объявление функции
    def is_prime(num):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count > 2 or num == 1:
            return False
        elif count == 2:
            return True

    while is_prime(num + 1) == False:
        num += 1
        continue
    return num + 1


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
