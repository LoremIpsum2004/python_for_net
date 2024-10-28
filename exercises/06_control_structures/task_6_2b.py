# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

correct_addr = False

while not correct_addr:
    ip = input("IP-адрес: ")
    
    if ip == '255.255.255.255':
        print('local broadcast')
        correct_addr = True
    elif ip == '0.0.0.0':
        print('unassigned')
        correct_addr = True
    else:
        try:
            if ip.count('.') != 3:
                raise ValueError()
            ip = ip.split('.')
            if len(ip) != 4:
                raise ValueError()
            for i in range(len(ip)):
                ip[i] = int(ip[i])
                if not (0 <= ip[i] <= 255):
                    raise ValueError()
        except ValueError:
            print('Неправильный IP-адрес')
        else:
            if 1 <= ip[0] <= 223:
                print('unicast')
            elif 224 <= ip[0] <= 239:
                print('multicast')
            else:
                print('unused')
            correct_addr = True