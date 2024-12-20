# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

strings = []
vlans = int(input('Какой VLAN показать: '))

with open('CAM_table.txt') as f:
    for line in f:
        if 'DYNAMIC' in line:
            strings.append(line.replace('DYNAMIC', '').split())
    
    for current_list in range(len(strings)):
        strings[current_list][0] = int(strings[current_list][0])
    strings.sort()

    for i in range(len(strings)):
        if strings[i][0] == vlans:
            print('{:<9}{:<14}{:>11}'.format(*strings[i]))