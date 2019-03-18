def gw(fn):#начальная сегментация текста на слова
    with open(fn, encoding="utf8") as file:
        t = file.read()
    t = t.replace("\n", " ")
    t = t.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "").replace("-", "")
    t = t.lower()
    w = t.split()
    w.sort()
    return w

def gwd(w): #получаем словарь из слов
    words_d = dict()
    for word in w:
        if word in words_d:
            words_d[word] = words_d[word] + 1
        else:
            words_d[word] = 1
    return words_d

def main():#функция вывода
    fn = input("Введите путь к файлу: ")
    w = gw(fn)
    words_d = gwd(w)
    print("Все слова:")
    for word in words_d:
        print(word.ljust(10), words_d[word]) 
    print("Количество слов: %d" % len(w))
    print("Количество уникальных слов: %d" % len(words_d))
if __name__ == "__main__":
    main()
