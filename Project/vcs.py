# Проект скрипта запуск которого автоматизирует вызов c сервера ВКС  терминалов видеоконферцсвязи  
# из заданного списка.
# При запуске скрипта необходимо выбрать заданный параметр (1/2), после чего, должно проходить 
# автоматическое подключение/отключение абонентов.
# 
#
from pprint import pprint
import re
import sys
# Задаем правила подключения
CMS_BASE = 'https://10.xxx.xxx.xxx:445/api/v1/'
CMS_HEADERS = {'Connect-type': 'application/json', 'autorization': "Basic XXXXXXXXXXXX=="}

# Задаем номера абонентов
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
            pprint (element)                    # Отслеживание работы скрипта
            connect = request.get(CMS_BASE + 'calllegs?filter=' + element, verify = false, headers=CMS_HEADERS)
            if  # ''.join(re.findall(r'callLegs total="(\d)', connect.text)) == '0':
                # request.post(CMS_BASE + 'calls/' + CallID + '/calllegs')  
            else :
                 print ("Абонент уже подключен - отмена")
      if str(action) == "2":                    # Отключение абонентов из списка
        for element in Party :
            pprint ("Отключаем абонента")
            pprint (element)
            connect = request.get()
            if  # ''.join(re.findall(r'callLegs total="(\d)', connect.text)) == '0'
            else :
                 print ("Абонент не подключен - отмена ") 
