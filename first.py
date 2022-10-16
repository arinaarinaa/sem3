#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.
spisok = [1,4,16,9]
result = 0
for i in range(len(spisok)):
    if not i%2==0:
        result += spisok[i]
print(result)