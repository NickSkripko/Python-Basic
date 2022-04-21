"""1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?"""

# import os
#
# """Проверил что нахожусь в нужной директории"""
# print('Текущая директория', os.getcwd())
# proj_start = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
# for root, folders in proj_start.items():
#     if os.path.exists(root):
#         print('Папка', root, 'уже существует')
#     else:
#         for folder in folders:
#             cur_dir = os.path.join(root, folder)
#             os.makedirs(cur_dir)


"""2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя."""

# import yaml
#
# new_starter = {'my_project':
#     [{'settings': [
#         '__init__.py', 'dev.py', 'prod.py'], },
#         {'mainapp': ['__init.py', 'models.py', 'views.py', {'templates': [{
#             'mainapp': ['base.html', 'index.html']}]}]},
#         {'authapp': ['__init.py', 'models.py', 'views.py', {'templates': [{
#             'authapp': ['base.html', 'index.html']}]}]}]}
# f = open('config.yaml', 'w')
# f.write(yaml.dump(new_starter))
# f.close()


"""3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). 
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках 
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, 
которая решена, например, во фреймворке django."""

# import os
# import shutil
#
# new_dir = 'templates'
# if not os.path.exists(new_dir):
#     os.mkdir(new_dir)
#
# directory = r'my_project'
# temp_files = []
#
# for r, d, f in os.walk(directory):
#     for file in d:
#         if '.html' in file:
#             temp_files.append(os.path.join(r, file))
# for path in temp_files:
#     directory_new = os.path.join(new_dir, os.path.basename(os.path.dirname(path)))
#     if not os.path.exists(directory_new):
#         os.mkdir(directory_new)
#     save_path = os.path.join(directory_new, os.path.basename(path))
#     shutil.copy(path, save_path)


"""4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница 
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), 
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт..."""

import os

temp_files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        temp_files.append(os.stat(file_path).st_size)
max_size = max(temp_files)

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 100
    out_dict[i] = 0

for file in temp_files:
    out_dict[100 ** len(str(file))] += 1

print(out_dict)