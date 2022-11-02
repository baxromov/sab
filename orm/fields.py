import re
class StringField:
    def __init__(self, max_length):
        self.max_length = max_length

    def __get__(self, instance, owner):
        return {
            "type": "varchar",
            "max_length": self.max_length,
            "row_query": f"varchar ({self.max_length})"
        }


class PrimaryKeyField:
    def __init__(self, auto_increment: bool = True):
        self.auto = auto_increment

    def __get__(self, instance, owner):
        data = {
            'type': 'INTEGER PRIMARY KEY',
            'auto_increment': self.auto,
            'row_query': "INTEGER PRIMARY KEY"
        }
        if self.auto:
            data['type'] += ' AUTOINCREMENT'
            data['row_query'] += ' AUTOINCREMENT'
        return data


class IntegerField:
    def __init__(self, null: bool = False):
        self.null = null

    def __get__(self, instance, owner):
        return {
            'type': 'INTEGER',
            'null': self.null,
            'row_query': f"INTEGER {'NOT NULL' if not self.null else ''}"
        }


class TextField:
    def __init__(self, null: bool = False):
        self.null = null

    def __get__(self, instance, owner):
        data = {
            'type': 'TEXT',
            'null': self.null,
            'row_query': "text "
        }
        if not self.null:
            data['row_query'] += 'NOT NULL'
        return data


class DecimalField:
    def __init__(self, max_digit: int, decimal_place: int, null: bool = False):
        self.null = null
        self.max = max_digit
        self.last = decimal_place

    def __get__(self, instance, owner):
        return {
            'type': 'decimal',
            'null': self.null,
            'max_digit': self.max,
            'decimal_place': self.last,
            'row_query': f"NUMERIC ({self.max}, {self.last})"
        }


class EmailField:
    def __init__(self, email):
        self.email = email
    def __get__(self, instance, owner):
        if re.match(r"^[a-z][a-zA-Z0-9_.][a-zA-z0-9_.]+@[a-z]{3}[a-z]+\.[a-z][a-z]+$", self.email):
            return True
        return False


class SmallIntegerField:
    def __get__(self, instance, owner):
        return {
            "type" : "SMALLINT",
            "row_query" : "SMALLINT"
        }


class PositiveIntegerField:
    def __init__(self, n: int):
        self.n = n
    def __get__(self, instance, owner):
         return 0 <= self.n <= 2147483647

class BigInteger:
    def __get__(self, instance, owner):
        return {
            "type" : "BIGINT",
            "row_query" : "BIGINT"
        }


class PositiveBigInteger:
    def __init__(self, n: int):
        self.n = n
    def __get__(self, instance, owner):
         return 0 <= self.n <= 18446744073709551615


class PhoneNumberField:
    def __init__(self, phone_number):
        self.phone = phone_number
    def __get__(self, instance, owner):
        if re.match(r"^\+[0-9]{1,4}[0-9]{8,13}$", self.phone):
            return True
        return False
