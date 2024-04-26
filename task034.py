
a = int(input("Введите пятизначное число "))
b = list(str(a))

c = int(input("На сколько пунктов сдвинуть вправо "))
n = c 
print(''.join(b[-n:] + b[:-n])) 
