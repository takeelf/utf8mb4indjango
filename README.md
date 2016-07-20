# utf8mb4indjango
utf8mb4 with mysqlclient in django



* Change my.cnf

[client]
default-character-set=utf8mb4

[mysql]
default-character-set=utf8mb4

[mysqld]
init-connect='SET NAMES utf8mb4'
character-set-client-handshake = FALSE
character-set-server=utf8mb4
collation-server=utf8mb4_unicode_ci



* Change mysql database and tables

ALTER DATABASE {database name} character set = utf8mb4 collate = utf8mb4_unicode_ci;
ALTER TABLE {table name} CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;




* Check

SHOW VARIABLES WHERE Variable_name LIKE 'character\_set\_%' OR Variable_name LIKE 'collation%';
select * from INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{database name}';
