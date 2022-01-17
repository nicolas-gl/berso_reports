import openpyxl
from access import dbx_token
from variables import sales_file_path, temp_sales_file_name


def copy_xls ():
    book = openpyxl.open(temp_sales_file_name, read_only=True)
    sheet = book.active

    # создаем список заголовков:
    columns = {}
    for now in range(len(sheet[1])):
        columns[sheet[1][now].value] = now
    # print(sheet['I1'].value)

# # ВАРИАНТ 1
#     # минусы: сложности с обработкой вывода
#     i = 1
#     for row in sheet:
#         columns_to_print = [0, 2, 3, 6, 7, 9, 10]
#         if row[columns['Выплачено?']].value == '-':
#             print(i, end=' ')
#             for c in columns_to_print:
#                 print(row[c].value, end=' ')
#             print()
#             i += 1

# ВАРИАНТ 2 (предпочтительный)
    # минусы: нагроможденный вывод
    i = 1
    for row in sheet:
        if row[columns['Выплачено?']].value == '-':
            print(
                i, ")  ",
                str(row[0].value)[0:11], "  ",
                row[2].value, " ",
                row[3].value, " за ",
                row[6].value, " (", 
                row[7].value, ")\nДолг: *", 
                row[9].value, " - ",
                row[10].value, "*\n",
                sep="")
            i += 1

# # ВАРИАНТ 3
#     # минусы: не работает
#     i = 1
#     columns_to_print = 0, 1
#     for row in sheet:
#         if row[columns['Выплачено?']].value == '-':
            

#             print("{0} — целое число, а {0} — строка.".format(columns_to_print))
            


copy_xls ()