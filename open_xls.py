import openpyxl
import dropbox_file_copy
from variables import local_sales_file_name


def make_report_text():
    dropbox_file_copy.download_sales()
    book = openpyxl.open(local_sales_file_name, read_only=True)
    sheet = book.active
    return_str = ''
    commitents = set()
    debts = {}
    
    for row in sheet:

        if row[9].value == '-':
            com = row[10].value
            sum = row[11].value
            ref = row[4].value
            name = row[3].value

            if com not in commitents:
                debts[com] = list()
                commitents.add(com)

            debts[com].append((sum, ref, name))

    for com in sorted(commitents):
        total_sum = 0  
        com_debts_str = ''
        text = ''

        for d in debts[com]:
            if d[0] != None:
                total_sum += d[0]
            else:
                com_debts_str += '↓↓↓ !ПРОВЕРИТЬ СУММУ! ↓↓↓\n'
            
            text += '{} р. - {}, {}\n'.format(
                d[0],                             # sum
                d[1],                             # ref
                d[2]                              # name
                )

        com_debts_str += '○ *{} - {} руб.*\n{}\n\n'.format(
            com, 
            total_sum,
            text
            )

        return_str += com_debts_str

    if return_str == '':
        return 'Нет долгов перед комитентами'
    return return_str
