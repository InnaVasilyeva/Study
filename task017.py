# Ввести с клавиатуры трехзначноре число и удалить у него среднюю цифру
a=input('Введите трехзначное число  ') 
L=list(a) 
d=L[0]+""+L[2]
print("Результат:  ", d)