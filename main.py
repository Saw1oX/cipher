key = [int(i) for i in input("введите ключ:").split()]
text = input("введите текст")


def litter(text, key, groupSize):
    if (len(text)%len(key)!=0):
        for i in range(len(key)-(len(text)%len(key))):
            text += str('#')
    return text
