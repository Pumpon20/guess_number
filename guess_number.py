import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Угадайте число от 1 до 100: "))
        attempts += 1

        if guess < number:
            print("Загаданное число больше.")
        elif guess > number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Вы угадали число за {attempts} попыток.")
            break

def main():
    print("Добро пожаловать в игру 'Угадай число'!")
    guess_number()

if __name__ == '__main__':
    main()
