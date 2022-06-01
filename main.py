key = [int(i) for i in input("введите ключ:").split()]
text = input("введите текст")
#mod: 1 - посимвольно, 2 - группы, 3 - слова

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
        text = text.split
        text += ['\0' for _ in range((lkey - (ltext % lkey)) % lkey]
    return text

