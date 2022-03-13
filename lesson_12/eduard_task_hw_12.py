"""
Сделать примеры в файлике:
1. __call__
2. __repr__
3. @classmethod &@staticmethod
4. @property, setter, deleter
"""


class Man:
    age = 23
    weight = 70
    growth = 180

    def __init__(self, hair: str = '', eyes: str = '', name: str = 'Abraham'):
        self.hair = hair
        self.eyes = eyes
        self.name = name

    def __repr__(self):
        return f"Меня зовут {self.name}"

    def __call__(self, *args, **kwargs):
        return print('Батя в здании!')

    @classmethod
    def up_age(cls, year: int):
        cls.age = year

    @staticmethod
    def all_man():
        return "Have Beard"

# CRUD

    @property
    def my_hair(self):
        return self.hair

    @my_hair.setter
    def my_hair(self, change):
        self.hair = change

    @my_hair.deleter
    def my_hair(self):
        del self.hair


man: Man = Man(name='Eduard')

man2: Man = Man(name="Vasya")
man()  # __call__
print(man)  # __repr__
man.up_age(24)  # classmethod
print(man.age)
print(man.weight)
man.my_hair = 'Black'  # Setter
print(man.my_hair)  # Getter

print(man2)
man2.up_age(30)
del man2.my_hair  # Del


print(Man().all_man())  # staticmethod
