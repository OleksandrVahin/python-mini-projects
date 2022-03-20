import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = []
include = [0] * 5


def get_yes_or_no():
    answer = input('Enter "yes" or "no"\n').lower().strip()
    while answer not in ['yes', 'no']:
        answer = input('Enter "yes" or "no"\n').lower().strip()
    if answer == 'yes':
        return True
    return False


def generate_password(length, chars):
    if include[4] == 1:
        d = [c for c in digits if c not in "il1Lo0O"]
        u = [c for c in uppercase_letters if c not in "il1Lo0O"]
        l = [c for c in lowercase_letters if c not in "il1Lo0O"]
        p = [c for c in punctuation if c not in "il1Lo0O"]
    else:
        d, u, l, p = digits, uppercase_letters, lowercase_letters, punctuation
    password = []
    if include[0] == 1:
        password.append(random.choice(d))
    if include[1] == 1:
        password.append(random.choice(u))
    if include[2] == 1:
        password.append(random.choice(l))
    if include[3] == 1:
        password.append(random.choice(p))
    if len(password) >= length:
        random.shuffle(password)
        return password[:length]
    else:
        password.extend(random.sample(chars, length - sum(include)))
        random.shuffle(password)
        return password


print('Ok, lets start creating\nSo some questions about your future password:')
print('How many passwords we will generate?')
amount = int(input())
print('What length should each password have?')
lengths = [int(input(f'{i + 1}) ')) for i in range(amount)]
print('Should the numbers "0123456789" be included?')
if get_yes_or_no():
    chars.extend(digits)
    include[0] = 1
print('Should uppercase "ABCDEFGHIJKLMNOPQRSTUVWXYZ" be included?')
if get_yes_or_no():
    chars.extend(uppercase_letters)
    include[1] = 1
print('Should lowercase "abcdefghijklmnopqrstuvwxyz" be included?')
if get_yes_or_no():
    chars.extend(lowercase_letters)
    include[2] = 1
print('Should the characters "!#$%&*+-=?@^_" be included?')
if get_yes_or_no():
    chars.extend(punctuation)
    include[3] = 1
print('Should ambiguous characters "il1Lo0O" be excluded?')
if get_yes_or_no():
    include[4] = 1
    chars = [c for c in chars if c not in "il1Lo0O"]

print('\tYour passwords:')
for i in range(amount):
    print(i + 1, ')\t', *generate_password(lengths[i], chars), sep='')
