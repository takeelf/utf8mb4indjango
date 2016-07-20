from MySQLdb import connections
from MySQLdb.connections import Connection
from _mysql_exceptions import NotSupportedError, OperationalError

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


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

