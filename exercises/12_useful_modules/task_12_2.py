# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress as ip

def convert_ranges_to_ip_list(input_list):
    output_list = []
    for addr in input_list:
        if not str(addr).count('-'):
            output_list.append(addr)
        elif str(addr).count('.') == 6:
            first_addr, last_addr = [int(ip.ip_address(x)) for x in str(addr).split('-')]

            for num in range(first_addr, last_addr + 1):
                output_list.append(str(ip.ip_address(num)))
        else:
            temp_list = addr.split('.')
            last_octet_list = temp_list.pop(-1).split('-')
            first_addr = int(ip.ip_address('.'.join(temp_list) + '.' + last_octet_list[0]))
            last_addr = int(ip.ip_address('.'.join(temp_list) + '.' + last_octet_list[1]))
            
            for num in range(first_addr, last_addr + 1):
                output_list.append(str(ip.ip_address(num)))

    return output_list

if __name__ == '__main__':
    my_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(convert_ranges_to_ip_list(my_list))