# utf8mb4indjango
utf8mb4 with mysqlclient in django



### Change my.cnf
```sh
[client]
default-character-set=utf8mb4

[mysql]
default-character-set=utf8mb4

[mysqld]
init-connect='SET NAMES utf8mb4'
character-set-client-handshake = FALSE
character-set-server=utf8mb4
collation-server=utf8mb4_unicode_ci
```


### Change mysql database and tables

 - ALTER DATABASE {database name} character set = utf8mb4 collate = utf8mb4_unicode_ci;
 - ALTER TABLE {table name} CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;




### Check

 - SHOW VARIABLES WHERE Variable_name LIKE 'character\_set\_%' OR Variable_name LIKE 'collation%';
 - select * from INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{database name}';



### Set settings.py
```sh
def _set_character_set(self, charset):
    """Set the connection character set to charset. The character
    set can only be changed in MySQL-4.1 and newer. If you try
    to change the character set from the current value in an
    older version, NotSupportedError will be raised."""
    if charset == "utf8mb4":
        py_charset = "utf8"
    else:
        py_charset = charset
    if self.character_set_name() != charset:
        try:
            super(Connection, self).set_character_set(charset)
        except AttributeError:
            if self._server_version < (4, 1):
                raise NotSupportedError("server is too old to set charset")
            self.query('SET NAMES %s' % charset)
            self.store_result()
        except OperationalError:
            if charset == "utf8mb4":
                self.query('SET NAMES %s' % charset)
                self.store_result()
    self.string_decoder.charset = py_charset
    self.unicode_literal.charset = py_charset

c = connections.Connection
c.set_character_set = _set_character_set

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dibiup',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
                    'init_command': 'SET '
                    'default_storage_engine=INNODB,'
                    'character_set_connection=utf8mb4,'
                    'collation_connection=utf8mb4_bin',
                    'charset': 'utf8mb4'
                    }
    }
}
```



