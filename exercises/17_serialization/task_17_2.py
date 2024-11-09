# -*- coding: utf-8 -*-
"""
Задание 17.2

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений
  и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv),
   в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена
  информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы (именно в этом порядке):
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается
на sh_vers. Вы можете раскомментировать строку print(sh_version_files),
чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
"""

import glob
import re
import csv

def parse_sh_version(input):
  '''
  Принимает вывод sh version строкой,
  возвращает (ios, image, uptime)
  '''
  result = []
  result.append(re.search(r'Cisco IOS Software, [^,]+, Version ([\w\.()]+), RELEASE SOFT', input).group(1))
  result.append(re.search(r'System image file is "([^"]+)"', input).group(1))
  result.append(re.search(r'router uptime is (.+)', input).group(1))
  return tuple(result)

def write_inventory_to_csv(data_filenames, csv_filename):
  '''
  Получает список файлов с выводом sh version и имя файла CSV для вывода,
  затем через parse_sh_version получаем ios, image и uptime. Также hostname
  из имени файла. Все это записывается в CSV файл согласно headers.
  sh_version_r3.txt
  '''
  with open(csv_filename, 'w', newline = '') as output:
    writer = csv.writer(output)
    writer.writerow(["hostname", "ios", "image", "uptime"])
    for file in data_filenames:
      row = []
      row.append(re.search(r'sh_version_([^\.]+).txt', file).group(1))
      row.extend(parse_sh_version(open(file).read()))
      writer.writerow(row)

sh_version_files = glob.glob("sh_vers*")
# print(sh_version_files)


if __name__ == '__main__':
  write_inventory_to_csv(['sh_version_r1.txt', 'sh_version_r2.txt', 'sh_version_r3.txt'], 'output.csv')
  pass