import sqlite3

from config import DATABASE


class Manager:
    def __get__(self, instance, owner):
        if instance is None:
            return QuerySet(owner)
        raise Exception("Error")


class QuerySet:
    __connection = None

    def __init__(self, name):
        self.name = name
        self.__connection = sqlite3.connect(DATABASE.get('db'))

    def execute(self, query):
        return self.__connection.execute(query)

    def make(self, cursor, query):
        temp = []
        for item in query:
            attrs = {}
            for index, key in enumerate(cursor.description):
                attrs.setdefault(key[0], item[index])
            temp.append(self.create_class(self.name.__name__, attrs))
        return temp

    @property
    def get_table(self):
        return self.name.__name__.lower()

    @staticmethod
    def create_class(class_name, attrs):
        return type(class_name, (), attrs)

    def all(self):
        query = f'select * from {self.get_table};'
        cursor = self.execute(query)
        query = cursor.fetchall()
        return self.make(cursor, query)

    def last(self):
        return self.execute(f"select * from {self.get_table} order by id desc limit 1;")

    def filter(self, **kwargs):
        t = " and ".join(f"{k}='{v}'" for k, v in kwargs.items())
        cmd = f"select * from {self.get_table} where {t};"
        cursor = self.execute(cmd)
        query = cursor.fetchall()
        return self.make(cursor, query)

    def get(self, **kwargs):
        """
        Faqat bitta ma'lumot qaytishi kerak
        :param kwargs:
        :return: Object
        """
        try:
            p = self.filter(**kwargs)
            if len(p) > 1: return "ERROR"
            return p[0]
        except:
            return None

    def create(self, **kwargs):
        """
        Ma'lumotlarni yaratish
        :param kwargs:
        :return:
        """
        insert = f"INSERT INTO {self.get_table}("
        values = 'VALUES ('
        for key, value in kwargs.items():
            insert += str(key) + ","
            values += f"'{str(value)}'" + ","
        insert = insert[:-1] + ") "
        values = values[:-1] + ")"
        sum = insert + "\n" + values + ";"
        print(sum)
        self.execute(sum)
        self.__connection.commit()
        return self.last()

    def delete(self, **kwargs):
        delete = f"DELETE FROM {self.name.__name__} WHERE "
        for key, value in kwargs.items():
            delete += f"{key}='{value}' AND "
        delete = delete[:-4]
        self.execute(delete)
        self.__connection.commit()

    def update(self, id: int, **kwargs):
        """
        update table_name
        set field_name1=value1, field_name2=value2
        where condition;
        :return:
        """
        query = f"update {self.get_table} set %s where id={id};"

        string_list: list = []
        for k, v in kwargs.items():
            string_list.append(f"{k}='{v}'")

        string: str
        string = ",".join(string_list)
        query = query % (string)
        self.execute(query)
        self.__connection.commit()
        return self.get(id=id)

    def get_or_create(self, **kwargs):
        if self.get(**kwargs):
            return False, self.get(**kwargs)
        return True, self.create(**kwargs)





class Model:
    __CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS %s (%s);'
    objects = Manager()

    def __init__(self, *args, **kwargs):
        if not self.__migrate__:
            print(f"Not migrated {self.__class__.__name__}")
        else:
            attrs = list(filter(lambda x: not x.startswith('_'), self.__dir__()))
            temp = []
            for item in attrs:
                q = f"{item} {getattr(self.__class__, item).get('row_query')}"
                temp.append(q)

            query = self.__CREATE_TABLE % (
                self.__class__.__name__.lower(),
                ",".join(temp)
            )
            self.__connection.execute(query)

    @property
    def __connection(self):
        if DATABASE.get('db'):
            return sqlite3.connect(DATABASE.get('db'))
        raise KeyError("Settingsda db keyi yo'q")
