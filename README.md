# Movigrama

A python module to help create plots of inventory in TOTVS ERP

#### Setup the project for windows users

To properly setup, it's necessary to create a INI 
file named `app_config.ini` with structure like 
the one presented bellow:

````ini
[ERP_SERVER]
driver = name of the driver, like: SQL Server
server = pointer to the server, like: db.domain.com
database = standard database
uid = user identification
pwd = password
````

After that, just click in `run.bat`

#### For MAC OS users
To use this project in MAC OS systems you should first ensure
your computer can access MS SQL Servers. To gain access to
that it's better to read this article:

Link: [Connecting to SQL Server from Mac OSX](https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Mac-OSX)

````
brew update
brew install unixodbc freetds
````

Also, you will need to have a new type of connection inside
your `app_config.ini` file. The new structure is:

````ini
[ERP_SERVER_MAC_OS]
server= pointer to the server, like: db.domain.com
database= standard database
user= user identification
tds_version='7.4'
password= password
port= port used by the server, usually: 1433
driver=driver location inside mac os, usually: /usr/local/lib/libtdsodbc.so
````

Author: Arnold Souza (arnoldporto@gmail.com), 2019
