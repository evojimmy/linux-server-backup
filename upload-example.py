# Example upload script (optional)
from scripts.uploads import FTP
def do(source_directory):
    return FTP("xxx.xx.xx.xx", "ftp_user", "password", source_directory)