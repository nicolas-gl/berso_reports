import dropbox
from variables import sales_file_path, local_sales_file_name
from access import dbx_token


dbx = dropbox.Dropbox(dbx_token)
def download_sales():
    with open(local_sales_file_name, "wb") as f:
        f.write(dbx.files_download(path=sales_file_path)[1].content)
