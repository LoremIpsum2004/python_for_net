# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
import ipaddress

def ping_ip_addresses(ip_list):
    available_list = []
    not_available_list = []

    for ip in ip_list:
        command = subprocess.run(['ping', str(ip)], stdout = subprocess.DEVNULL)
        if command.returncode == 0:
            available_list.append(ip)
        else:
            not_available_list.append(ip)

    return tuple([available_list, not_available_list])

if __name__ == '__main__':
    addr1 = ipaddress.ip_address('192.168.0.1')
    addr2 = ipaddress.ip_address('192.168.0.2')
    addr3 = ipaddress.ip_address('192.168.0.3')
    print(ping_ip_addresses([addr1, addr2, addr3]))