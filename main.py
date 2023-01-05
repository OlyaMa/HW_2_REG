from pprint import pprint
from re import sub
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
for x in contacts_list:
  if len(x) > 7:
    del x[7:]
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# Замена номеров
num_pattern = r'(8|\+7)\s*\(*(\d{3})\)*[\s|-]*(\d{3})[\s|-]*(\d{2})[\s|-]*(\d{2})\s*\(*(доб.)?\s*(\d{4})?\)*'
new_num_pattern = r'+7(\2)\3-\4-\5 (\6\7)'
contacts_list_new = list()
for page in contacts_list:
  page_string = ','.join(page) # объединяем в строку
  f_page = sub(num_pattern, new_num_pattern, page_string) # заменяем шаблоны в строке
  pat = r'\s\(\)'
  new_pat = r''
  format_page = sub(pat, new_pat, f_page) # удаляем ()
  page_list = format_page.split(',') # формируем список строк
  contacts_list_new.append(page_list)
# pprint(contacts_list_new)

# Расстановка ФИО
name_pattern = r'^(\w+)(\s*)(\,?)(\w+)' \
                   r'(\s*)(\,?)(\w*)(\,?)(\,?)(\,?)'
name_pattern_new = r'\1\3\10\4\6\9\7\8'
contacts_list = list() # создаем список
for page in contacts_list_new:
  page_string = ','.join(page) # объединяем в строку
  format_page = sub(name_pattern, name_pattern_new, page_string)
  page_list = format_page.split(',') # формируем список строк
  contacts_list.append(page_list)
# pprint(contacts_list)

# Удаление дубликатов
for i in contacts_list:
  for j in contacts_list:
    if i[0] == j[0] and i[1] == j[1] and i != j:
      if i[2] == '':
        i[2] = j[2]
      if i[3] == '':
        i[3] = j[3]
      if i[4] == '':
        i[4] = j[4]
      if i[5] == '':
        i[5] = j[5]
      if i[6] == '':
        i[6] = j[6]
    contact_list = list()
    for page in contacts_list:
      if page not in contact_list:
        contact_list.append(page)
# pprint(contact_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contact_list)
