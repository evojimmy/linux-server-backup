#!/usr/bin/env python

import config

def _now():
    from time import strftime
    return strftime('%Y-%m-%d %H:%M:%S')

def do():
    # Set environments
    from time import strftime
    backup_time = strftime('%Y-%m-%d_%H-%M-%S')
    import os
    backup_path = os.getcwd() + os.sep + 'backups' + os.sep + backup_time
    os.system('mkdir -p %s' % backup_path)
    import logging
    log_file = backup_path + os.sep + 'log.txt'
    logging.basicConfig(filename=log_file, format='%(message)s', level=logging.INFO)
    import config
    logging.info('[SITEBAK-INFO] Start backup at %s' % _now())

    # Dump MYSQL
    logging.info('[SITEBAK-INFO] Start dumping MySQL at %s' % _now())
    from scripts import mysqldump
    log = mysqldump.do(user=config.MYSQLDUMP['user'],
                       password=config.MYSQLDUMP['password'],
                       outpath=backup_path)
    logging.info(log)
    logging.info('[SITEBAK-INFO] Finish dumping MySQL at %s' % _now())

    # Backup engine configuration
    logging.info('[SITEBAK-INFO] Start backing up Apache configuration at %s' % _now())
    from scripts import filebackup
    log = filebackup.do(filelist=config.ENGINE_FILES, outpath=backup_path,
                        name='engine')
    logging.info(log)
    logging.info('[SITEBAK-INFO] Finish backing up Apache configuration at %s' % _now())


    # Backup selected files
    from scripts.widgets.BaseWidget import BaseWidget
    web_files = []
    for f in config.WEB_FILES:
        if isinstance(f, BaseWidget):
            for ff in f.expand():
                web_files.append(ff)
        elif isinstance(f, str):
            web_files.append(f)
    logging.info('[SITEBAK-INFO] Start backing up user contents at %s' % _now())
    log = filebackup.do(filelist=web_files, outpath=backup_path,
                        name='web_contents', compress_type='gz')
    logging.info(log)
    logging.info('[SITEBAK-INFO] Finish backing up user contents at %s' % _now())

    # Backup config.py in this dir
    logging.info('[SITEBAK-INFO] Start backing up config.py at %s' % _now())
    config_file = os.getcwd() + os.sep + 'config.py'
    log = filebackup.do(filelist=(config_file,), outpath=backup_path,
                        name='config_py')
    logging.info(log)
    logging.info('[SITEBAK-INFO] Finish backing up config.py at %s' % _now())

if __name__ == '__main__':
    do()
