def bin_choice(a, b):
    answer = input(f'Enter "{a}" or "{b}"\n').lower().strip()
    while answer not in [a, b]:
        answer = input(f'Enter "{a}" or "{b}"\n').lower().strip()
    if answer == a:
        return True
    return False


def algorythm(language, key, text):
    result = []
    if language:
        for c in text:
            if c.isalpha() and c.islower():
                c = chr((ord(c) - ord('a') + key) % 26 + ord('a'))
            elif c.isalpha() and c.isupper():
                c = chr((ord(c) - ord('A') + key) % 26 + ord('A'))
            result.append(c)
    else:
        for c in text:
            if c.isalpha() and c.islower():
                c = chr((ord(c) - ord('а') + key) % 32 + ord('а'))
            elif c.isalpha() and c.isupper():
                c = chr((ord(c) - ord('А') + key) % 32 + ord('А'))
            result.append(c)
    result = ''.join(result)
    return result


print("Hello, it is program which help you to code and decode text via Caesar cipher")
print('So, what do yo want?')
direction = bin_choice('code', 'decode')
print('What is language of the text, English or Russian?')
language = bin_choice('en', 'ru')
key = input('Enter the shift\n')
while not key.isdigit():
    print('Enter the positive integer')
    key = input('Enter the shift\n')
else:
    key = int(key)
txt = input('Enter text:\n')
if direction:
    result = algorythm(language, key, txt)
    print('After coding:', result, sep='\n')
else:
    result = algorythm(language, -key, txt)
    print('After decoding:', result, sep='\n')
