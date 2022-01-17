import openpyxl
from variables import sales_file_path, temp_sales_file_name


def copy_xls ():
    book = openpyxl.open(temp_sales_file_name, read_only=True)
    sheet = book.active

    # создаем список заголовков:
    columns = {}
    for now in range(len(sheet[1])):
        columns[sheet[1][now].value] = now

    print(sheet['I1'].value)

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

    # print(sheet.max_row)
    # print(sheet[1034][3].value)

    # пока хз, зачем написал это

copy_xls ()