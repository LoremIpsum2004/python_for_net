# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re
from pprint import pprint

def parse_sh_cdp_neighbors(input):
    result = {}
    hostname = re.match(r'\n?([^>#]+)(?:>|#)show cdp neighbors', input).group(1)
    result[hostname] = {}
    #R1           Eth 0/1         122           R S I           2811       Eth 0/0
    regex = re.compile(r'(?P<device_id>\S+) +(?P<local_interface>(?:Eth|Fa) [0-9/]+).+(?P<port_id>(?:Eth|Fa) [0-9/]+)')
    for enter in regex.finditer(input):
        result[hostname][enter.group('local_interface')] = {enter.group('device_id'): enter.group('port_id')}
    return result

input = '''
SW1>show cdp neighbors

Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R1           Eth 0/1         122           R S I           2811       Eth 0/0
R2           Eth 0/2         143           R S I           2811       Eth 0/0
R3           Eth 0/3         151           R S I           2811       Eth 0/0
R4           Eth 0/4         150           R S I           2811       Eth 0/0
'''
if __name__ == '__main__':
    pprint(parse_sh_cdp_neighbors(input))
    pass