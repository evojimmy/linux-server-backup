LAMP server backup tool
=========================

## Description

This tool backs up:

+ Web engine configuration (apache, php, ...)
+ All databases in MySQL
+ Selected web contents
+ Configuration file for this tool

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

````
./immediate_backup.py
````
