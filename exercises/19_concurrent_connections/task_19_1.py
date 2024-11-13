# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""

import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def is_ip_reachable(ip):
    '''
    Принимает string ip, возвращает
    код завершения ping'а
    '''

    return subprocess.run(['ping', ip], stdout = subprocess.DEVNULL).returncode

def ping_ip_addresses(ip_list, limit = 3):
    reachable, unreachable = [], []
    with ThreadPoolExecutor(max_workers = limit) as execute:
        return_code_list = execute.map(is_ip_reachable, ip_list)
        for ip, code in zip(ip_list, return_code_list):
            if code == 0:
                reachable.append(ip)
            else:
                unreachable.append(ip)
    return (reachable, unreachable)

test_list = ['192.168.100.1', '192.168.100.16', '192.168.100.3', '192.168.100.29',]

if __name__ == '__main__':
    time1 = datetime.now()
    print(ping_ip_addresses(test_list, limit = 4))
    time2 = datetime.now()
    print(ping_ip_addresses(test_list, limit = 1))
    print(time2 - time1, datetime.now() - time2, sep = '\t')