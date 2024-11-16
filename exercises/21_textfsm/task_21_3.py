# -*- coding: utf-8 -*-
"""
Задание 21.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами.
  Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
"""
from textfsm import clitable
from netmiko import ConnectHandler

def parse_command_dynamic(command_output, attributes_dict, index_file = 'index', templ_path = 'templates'):
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    
    header = list(cli_table.header)
    data_rows = [list(row) for row in cli_table]
    result = []
    for row in data_rows:
       result.append(dict(zip(header, row)))
    return result

if __name__ == '__main__':
    r1_params = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    attribute_dict = {
        'Command': 'sh ip int br',
        'Vendor': 'cisco_ios'
    }
    with ConnectHandler(**r1_params) as ssh:
      ssh.enable()
      output = ssh.send_command('sh ip int br')
      print(parse_command_dynamic(output, attribute_dict))