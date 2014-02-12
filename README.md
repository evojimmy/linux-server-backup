Linux server backup
======================

## Description

This tool backs up:

+ Web engine configuration (apache, php, ...)
+ All databases in MySQL
+ Selected web contents
+ Configuration file for this tool

Automatic backup can be set running in background.

## Feature

+ Automatic backup in background.
+ Special optimized for PHP applications like Wordpress.
+ FTP upload backup to cloud storage

## Preparation

#### Prerequisites

+ Python 2.7
+ lftp (required by FTP upload)

#### Setting up backup user for MySQL

from: http://blog.roozbehk.com/post/25580691418/mysql-user-to-backup-databases

````
CREATE USER 'dbbackup'@'localhost' IDENTIFIED BY  '***';

GRANT SELECT , 
RELOAD , 
FILE , 
SUPER , 
LOCK TABLES , 
SHOW VIEW ON * . * TO  'dbbackup'@'localhost' IDENTIFIED BY  '***' WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0 ;
````

#### Create `config.py`

Rename `config-example.py` to `config.py` and replace the content properly.

#### Create `upload.py` (optional)

If automatically upload is needed, 
rename `upload-example.py` to `upload.py` and replace the content properly.


## Usage

#### Immediate backup

````
./immediate_backup.py
````

#### Routine backup

````
./routine_backup.sh {start|stop|status}
````

First backup will not take place immediately. For example, if `config.ROUTINE_DAYS`
is set to 7, the first backup will start after 7 days.

The log is written into `routine_backup.log`.
