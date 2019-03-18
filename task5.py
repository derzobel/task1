print ("Введите строку:\n")
st = input()
st = st.replace("\n", " ")
st = st.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "").replace("-", "")
st = st.lower()
st = st.split()
st.sort()
words_d = dict()
for word in st:
    if word in words_d:
        words_d[word] = words_d[word] + 1
    else:
        words_d[word] = 1
print("Количество уникальных слов: %d" % len(words_d))
kk = words_d.keys()
print(kk)
