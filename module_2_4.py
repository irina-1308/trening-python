numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#Простые числа - это натуральные числа больше единицы, которые делятся нацело только на единицу и на себя.
# Например, число 3 простое, так как нацело делится только на 1 и 3. Число 4 сложное,
# так как нацело делится не только на 1 и 4, но также на число 2.
primes = [] #2.1
not_primes = [] #2.1

for number in numbers: #2.2
    #print(number)
    if number == 1: #2.3
        continue
    is_prime = True #2.4
    for i in range(2, number):
        if number % i == 0: # если исходное число делится на какое-либо отличное от 1 и самого себя
            is_prime = False
            break             # останавливаем цикл, если встретили делитель числа
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print("Primes:", primes)
print("Not Primes:", not_primes)