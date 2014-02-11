# Example configuration file.
from scripts.widgets import *

MYSQLDUMP = {
    'user': 'backup',
    'password': 'backup'
}

## Be sure that ENGINE_FILES and WEB_FILES are lists of folders or files.

ENGINE_FILES = ('/path/to/apache/conf', '/path/to/php/ini')

WEB_FILES = (
'/path/to/web/contents',
Wordpress('/path/to/wordpress/root')
)
