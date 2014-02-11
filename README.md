LAMP server backup tool
=========================

## Description

This tool backs up:

+ Web engine configuration (apache, php, ...)
+ All databases in MySQL
+ Selected web contents
+ Configuration file for this tool

Automatic backup can be set running in background.

## Preparation

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

#### Write `config.py`

Rename `config-example.py` to `config.py` and replace the content properly.

## Usage

#### Immediate backup

````
./immediate_backup.py
````

#### Routine backup

````
./routine_backup.sh
````

First backup will not talk place immediately. For example, if `config.ROUTINE_DAYS`
is set to 7, the first backup will start after 7 days.

The log is written into `routine_backup.log`.
