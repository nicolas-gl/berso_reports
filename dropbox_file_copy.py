import dropbox
from access import dbx_token
from variables import sales_file_path, temp_sales_file_name


dbx = dropbox.Dropbox(dbx_token)


with open(temp_sales_file_name, "wb") as f:
    f.write(dbx.files_download(path=sales_file_path)[1].content)

print('got_it')
