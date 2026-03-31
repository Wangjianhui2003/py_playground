# for
words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word)

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
    print(user + "--" + status)

# range

for i in range(5):
    print(i)

print(range(3))
print(range(3, 12))
print(range(3, 12, 4))

print(list(range(3)))
print(list(range(3, 12)))
print(list(range(3, 12, 4)))

# In many ways the object returned by range() behaves as if it is a list,
# but in fact it isn’t. It is an object which returns the successive items
# of the desired sequence when you iterate over it, but it doesn’t
# really make the list, thus saving space.

# We say such an object is iterable, that is,
# suitable as a target for functions and constructs that expect something
# from which they can obtain successive items until the supply is exhausted.
# We have seen that the for statement is such a construct,
# while an example of a function that takes an iterable is sum():
print(sum(range(5)))

# ========================================4.5 else clauses for loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# ========================================4.6 pass
def func1():
    ...


def func2():
    pass


# ========================================4.7 match

# for语句不会创建块级作用域，所以前面的for语句用过的status变量会留在外层，后面的语句用到了status变量，会覆盖
def http_error(status_code):
    match status_code:
        case 200:
            print("ok")
        case 400:
            print("bad request")
        case 401 | 403 | 404:
            print("not allowed")
        case _:
            print("other error")


http_error(400)
http_error(401)
http_error(404)


# use class + match
class Point:
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


from enum import Enum


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")


# ======================================== 4.8 Definition Functions


# The execution of a function introduces a new symbol table used
# for the local variables of the function. More precisely, all
# variable assignments in a function store the value in the local
# symbol table; whereas variable references first look in the local
# symbol table, then in the local symbol tables of enclosing functions,
# then in the global symbol table, and finally in the table of built-in names.
# Thus, global variables and variables of enclosing functions cannot
# be directly assigned a value within a function
# (unless, for global variables, named in a global statement, or,
# for variables of enclosing functions, named in a nonlocal statement),
# although they may be referenced.

def fib(n):
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

f = fib
print(fib)
f(20)
print(fib(20))

# ======================================== 4.9 more detail about function

# The default values are evaluated at the point of function definition in the defining scope, so that
i = 5

def f(arg=i):
    print(arg)

i = 6
f() # 5

# when default value is a mutable object
def f2(a, Ls=[]):
    Ls.append(a)
    return Ls

print(f2(1))
print(f2(2))
print(f2(3))

def f3(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f3(1))
print(f3(2))
print(f3(3))
