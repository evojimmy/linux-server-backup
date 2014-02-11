# Example configuration file.
from scripts.widgets import *

MYSQLDUMP = {
    'user': 'backup',
    'password': 'backup'
}

## Be sure that APACHE_FILES and WEB_FILES are lists of folders or files.

APACHE_FILES = ('/path/to/apache/conf', )

WEB_FILES = (
'/path/to/web/contents',
Wordpress('/path/to/wordpress/root')
)
