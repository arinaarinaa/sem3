#Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input('dlina - \n'))
spisok = []
for i in range(n):
    spisok.append(int(input()))
print(spisok)

spisok2 = []
for i in range(len(spisok)):
    while i <len(spisok)/2 and n>len(spisok)/2:
        n = n-1
        a = spisok[i]* spisok[n]
        spisok2.append(a)
        i+=1

print(spisok2)