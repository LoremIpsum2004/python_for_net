# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re
from pprint import pprint

def convert_ios_nat_to_asa(input_file, output_file):
    with open(input_file) as input, open(output_file, 'w') as output:
        regex = re.compile(r'(?P<ip>[\d.]+) (?P<port_in>\d+) interface \S+ (?P<port_out>\d+)')
        result = []
        for line in input:
            match = regex.search(line)
            if match:
                str = f'object network LOCAL_{match['ip']}\n' \
                      f' host {match['ip']}\n' \
                      f' nat (inside,outside) static interface service tcp {match['port_in']} {match['port_out']}\n'
                result.append(str)
        output.writelines(result)
    return None


if __name__ == '__main__':
    convert_ios_nat_to_asa('cisco_nat_config.txt', 'output.txt')