import re
from pprint import pprint

import csv

PHONE_PATTERN = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
SUB_PHONE = r'+7(\3)\6-\8-\10 \12\13'


with open("phonebook_raw.csv", encoding= 'utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)



new_contacts_list = list()
for contact in contacts_list:
    new_contact = list()
    full_name_str = ",".join(contact[:3])
    result = re.findall(r'(\w+)', full_name_str)
    while len(result) < 3:
      result.append('')
    new_contact += result
    new_contact.append(contact[3])
    new_contact.append(contact[4])
    phone_pattern = re.compile(PHONE_PATTERN)
    changed_phone = phone_pattern.sub(SUB_PHONE, contact[5])
    new_contact.append(changed_phone)
    new_contact.append(contact[6])
    new_contacts_list.append(new_contact)


phone_book = dict()
for contact in new_contacts_list:
    if contact[0] in phone_book:
        contact_value = phone_book[contact[0]]
        for i in range(len(contact_value)):
            if contact[i]:
                contact_value[i] = contact[i]
    else:
         phone_book[contact[0]] = contact
phonebook = list(phone_book.values())

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(phonebook)