# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    access_dict = dict()
    trunk_dict = dict()
    current_int = None

    with open(config_filename) as f:
        for line in f:
            if 'interface ' in line:
                current_int = line.split()[-1]
            elif 'switchport access vlan' in line:
                access_dict[current_int] = int(line.split()[-1])
            elif 'switchport trunk allowed vlan' in line:
                trunk_dict[current_int] = [int(num) for num in line.split()[-1].split(',')]
            elif 'switchport mode access' in line:
                access_dict.setdefault(current_int, 1)

    return tuple([access_dict, trunk_dict])

print(get_int_vlan_map('config_sw2.txt'))