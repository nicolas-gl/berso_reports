import openpyxl
import dropbox_file_copy
from variables import local_sales_file_name


def make_report_text():
    dropbox_file_copy.download_sales()
    book = openpyxl.open(local_sales_file_name, read_only=True)
    sheet = book.active
    return_str = ''

    for row in sheet:
        if row[8].value == '-':                             #проверка на невыплату
            a = '○  *{} - {} руб.*\n{} - {} \n\n'.format(
                row[9].value,                               # комитент
                row[10].value,                              # сумма комитенту
                row[3].value,                               # артикул
                row[2].value,                               # название предмета
                )
            return_str += a
    if return_str == '':
        return 'Нет долгов перед комитентами'

    return return_str
