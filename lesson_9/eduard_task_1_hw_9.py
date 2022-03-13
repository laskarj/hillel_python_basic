"""
a = []
b = a
a.append('asdf')
print(b)
"""


def one():
    x = ['one', 'two']

    def inner():
        print(x)
        print(id(x))
    return inner


o = one()

print(o())
print(dir(o()))

print(o.__closure__[0])

print(id(o.__closure__[0]))

print(dir(o.__closure__[0].cell_contents))

a = o.__closure__[0].cell_contents

a.append('asdf')
print(id(a))
print(a)
print(o())

