# Номер автомобиля указан верно или нет
import re
i=input("Введите номер автомобиля формата X123XX123 ", )
r=re.compile(r'(\w{1}).*?(\d{3}).*?(\w{2}).*?(\d{2})')
if re.match(r,i):
    print('Верно')
else:
    print('Не верно')