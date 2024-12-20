# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
str = input('Введите IP-сеть: ')

border = str.find('/')
net = str[:border].split('.')
mask = int(str[border + 1:])

net = [ int(x) for x in net ] # Переводим все строки-октеты адреса в int

net = list('{:>08b}{:>08b}{:>08b}{:>08b}'.format(*net))
del net[mask:]
net = ''.join(net) + '0' * (32 - mask)

print('\nNetwork:')
print('{0:<10}{1:<10}{2:<10}{3:<10}\n{0:>08b}  {1:>08b}  {2:>08b}  {3:>08b}'.format(int(net[:8], 2), int(net[8:16], 2), int(net[16:24], 2), int(net[24:], 2)))


full_mask = mask * '1' + (32 - mask) * '0'

print('\nMask:\n/{}'.format(mask))
print('{0:<10}{1:<10}{2:<10}{3:<10}\n{0:>08b}  {1:>08b}  {2:>08b}  {3:>08b}'.format(int(full_mask[:8], 2), int(full_mask[8:16], 2), int(full_mask[16:24], 2), int(full_mask[24:], 2)))