from functools import lru_cache, total_ordering, singledispatch


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print([fib(n) for n in range(16)])
print(fib.cache_info())


############################################
print('-' * 100)
############################################


@total_ordering
class Student:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
               (other.lastname.lower(), other.firstname.lower()))


student1 = Student('Zenke', 'Bartosz')
student2 = Student('Martyniuk', 'Zenek')

print("Bartek >  Zenek  ", student1 > student2)
print("Bartek <  Zenek  ", student1 < student2)
print("Bartek == Zenek  ", student1 == student2)
print("Bartek <= Zenek  ", student1 <= student2)
print("Bartek >= Zenek  ", student1 >= student2)


############################################
print('-' * 100)
############################################


@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)


fun('string', True)
fun(12, True)
fun(['l', 'i', 's', 't'], True)
