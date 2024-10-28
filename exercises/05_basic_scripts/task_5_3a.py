# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
    'Введите номер VLAN: '
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
    'Введите разрешенные VLANы: '
]

mode_dict = dict(access = access_template, trunk = trunk_template)

mode = input('Введите режим работы интерфейса (access/trunk): ')
intf = input('Введите тип и номер интерфейса: ')
vlans = input(mode_dict[mode][-1])
del mode_dict[mode][-1]


final_str = '''
interface {}
{}
'''

print(final_str.format(intf, '\n'.join(mode_dict[mode]).format(vlans)))