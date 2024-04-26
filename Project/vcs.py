# Проект скрипта запуск которого автоматизирует вызов c сервера ВКС  терминалов видеоконферцсвязи  
# из заданного списка.
# При запуске скрипта необходимо выбрать параметр (1/2) в зависимости от подключения/отключения 
# абонентов
 
from pprint import pprint
import re
import sys
import requests
# Задаем правила подключения
CMS_BASE = 'https://10.xxx.xxx.xxx:445/api/v1/'
CMS_HEADERS = {'Connect-type': 'application/json', 'autorization': "Basic XXXXXXXXXXXX=="}

# Задаем список абонентов для подключения
Party = [
    '2265'
    '384058'
    '7370'
    '180167'
    '2377'
] 
# Определяем функцию, которую будет удобно вызывать для подключения / отключения абонентов
def autoconnect(action) :
      pprint(action)
      if str(action) == "1" :                   # Подключение абонентов из списка
        for element in Party :     
            pprint ("Подключаем абонента")
            pprint (element)                    # Проверка подключения абонента
            connect = requests.get(CMS_BASE + 'calllegs?filter=' + element, verify = false, headers=CMS_HEADERS)
            if  # ''.join(re.findall(r'callLegs total="(\d)', connect.text)) == '0':
                # requests.post(CMS_BASE + 'calls/' + CallID + '/calllegs')  
            else :
                 print ("Абонент уже подключен - отмена")
      if str(action) == "2":                    # Отключение абонентов из списка
        for element in Party :
            pprint ("Отключаем абонента")
            pprint (element)
            connect = requests.get(CMS_BASE + 'calllegs?filter=' + element, verify = false, headers=CMS_HEADERS)
            if  # ''.join(re.findall(r'callLegs total="(\d)', connect.text)) == '0':
                # cleg =''.join(refindall(r'callleg id="(\w+\-\w+\-\w+\-\w+\-\w+\)', connect.text)) 
                # requests.delete(CMS_BASE + 'calls/' + CallID + '/calllegs') 
            else :
                 print ("Абонент не подключен - отмена ") 

print ("Выберите операцию и нажмите enter: ")
print (" 1 - автоматическое подключеие абонентов")
print (" 2 - автоматическое отключение абонентов")
actiontype = int(sys.stdin.readline())
autoconnect(actiontype)