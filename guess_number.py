import random

n = 100
num = random.randint(1, n)
counter = 0
print('Добро пожаловать в числовую угадайку')


def is_valid(text):
    if text.isdigit() and '.' not in text and 1 <= int(text) <= n:
        return True
    return False


def new_game():
    global counter, num, n
    counter = 0
    print('Хотите изменить диапозон угадывания?')
    if get_yes_or_no():
        while True:
            k = input('Введите новую границу\n')
            if k.isdigit() and '.' not in k and int(k) > 1:
                n = int(k)
            else:
                print('А может быть все-таки введем целое число больше единицы?')
                continue
        num = random.randint(1, n)


def get_yes_or_no():
    answer = input('Введите "да" или "нет"\n').lower().strip()
    while answer not in ['да', 'нет']:
        answer = input('Введите "да" или "нет"\n').lower().strip()
    if answer == 'да':
        return True
    return False


while True:
    guess = input(f'Введите число от 1 до {n}\n')
    if is_valid(guess):
        guess = int(guess)
    else:
        print(f'А может быть все-таки введем целое число от 1 до {n}?')
        continue
    counter += 1
    if guess > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    if guess < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    if guess == num:
        print('Вы угадали, поздравляем!')
        if counter % 10 == 1:
            print('Вы отгадали за', counter, 'попытку')
        else:
            print('Вы отгадали за', counter, 'попыток')
        print('Хотите сыграть еще раз?')
        if get_yes_or_no():
            new_game()
            continue
        else:
            break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
