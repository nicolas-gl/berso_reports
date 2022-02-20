import openpyxl
import dropbox_file_copy
from variables import local_sales_file_name


def make_report_text():
    book = openpyxl.open(local_sales_file_name, read_only=True)
    sheet = book.active

    # создаем список заголовков:
    columns = {}
    for now in range(len(sheet[1])):
        columns[sheet[1][now].value] = now

    i = 1
    return_str = ''
    for row in sheet:
        if row[columns['Выплачено?']].value == '-':
            a = '{})  {}  {} {} за {} ({})\nДолг: *{} - {}*\n\n'.format(
                i,
                str(row[0].value)[0:11],
                row[2].value,
                row[3].value,
                row[6].value,
                row[7].value,
                row[9].value,
                row[10].value
                )
            return_str += a
            i += 1
    if return_str == '':
        return 'Нет долгов перед комитентами'
    # почему-то не работает удаление пробелов в конце. Разобраться
    return_str.rstrip()
    return return_str
