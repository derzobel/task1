print("Введите строку.\n")
st = input()
l = st.split()
for j in range(0,len(l)):
    l[j]*=2
    print(l[j], end = ' ')
