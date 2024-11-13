# -*- coding: utf-8 -*-
"""
Задание 19.2

Создать функцию send_show_command_to_devices, которая отправляет одну и ту же
команду show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя текстового файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в обычный текстовый файл в таком формате
(перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""

import yaml
from concurrent.futures import ThreadPoolExecutor, as_completed
from netmiko import ConnectHandler


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        #print(ssh.send_command(command, strip_prompt = False, strip_command = False))
        result = ssh.send_command(command, strip_command = False, strip_prompt = False)
    return ''.join(reversed(result[:result.rfind('\n'):-1])) + result[:result.rfind('\n')] # Перемещаю hostname# в начало


def send_show_command_to_devices(devices, command, filename, limit = 3):
    with open(filename, 'w') as f, ThreadPoolExecutor(max_workers = limit) as executor:
        future_output = [ executor.submit(send_show_command, device, command) for device in devices ]
        for out in as_completed(future_output):
            f.write(out.result() + '\n')

if __name__ == '__main__':
    send_show_command_to_devices(yaml.safe_load(open('devices.yaml')), 'sh ip int br', 'output.txt')