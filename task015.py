# Ввести с клавиатуры трехзначное число и перевернуть его 

a=input('Введите трехзначное число  ') 
L=list(a) 
M=''.join(reversed(L))
print("Результат:  ", M)
