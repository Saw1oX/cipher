def litter(text, key, group_len, mod):
    lkey = len(key)
    ltext = len(text)
    if mod == 1:
        for i in range(len(key) - (len(text) % len(key))):
            text += str('/0')
    elif mod == 2:
        for f in range(lkey * group_len - ltext):
            text += str('/0')
        text = [text[i:i + group_len] for i in range(0, len(text), group_len)]
    elif mod == 3:
        probel = ' '
        text = text.split()
        text += ['\0' for k in range((lkey - (ltext % lkey)) % lkey)]
    return text

def encryption(text, key, mod, group_len):
    lkey = len(key)
    ltext = len(text)
    probel = ''
    text = litter(text, key, group_len, mod)
    text = [text[i:i + lkey] for i in range(0, len(text), lkey)]
    result = probel.join([probel.join([text_part[key.index(str(i))] for i in range(lkey)]) for text_part in text])
    return result

def recryption(text, key, mod, group_len):
    lkey = len(key)
    ltext = len(text)
    probel = ''
    text = litter(text, key, group_len, mod)
    text = [text[i:i + lkey] for i in range(0, len(text), lkey)]
    result = probel.join([probel.join([text_part[int(i)] for i in key]) for text_part in text]).replace(
            '\0', '')
    return result

print("что вы хотите сделать?\n", "1 - зашифровать\n", "2 - расшифровать")
er = int(input())
print("выберите вид шифрования: \n", "1 - посимвольно\n", "2 - группа символов\n", "3 - по словам")
mod = int(input())
if mod == 2:
    group_len = int(input("количество символов в блоке: "))
else:
    group_len = 1
text = input("Введите текст: ")
key = input('Введите ключ (через пробел, например - 3 0 1 2):').split(' ')
if er == 1:
    print(encryption(text, key, mod, group_len))
elif er ==2:
    print(recryption(text, key, mod, group_len))
