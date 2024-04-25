import csv
a=input('Введите название файла: ' )
file1 = open (a+'.csv','w',encoding='UTF-8',newline='')
wr = csv.writer(file1,delimiter='|')
dt = [['1','Апельсины','100'],['2','Мандарины','200'],['3','Лимоны   ','100']]
for row in dt:
    wr.writerow(row)
file1.close()
    