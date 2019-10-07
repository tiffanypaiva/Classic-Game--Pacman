import collections
import math
import os


def floor(Value, Size, Offset=200):

    return float(((Value + Offset) // Size) * Size - Offset)


def path(filename):
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    fullpath = os.path.join(dirpath, filename)
    return fullpath




def square(x, y, Size, name):

    import turtle
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(name)
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(Size)
        turtle.left(90)

    turtle.end_fill()
def line(a, b, x, y):
    import turtle
    turtle.up()
    turtle.goto(a, b)
    turtle.down()
    turtle.goto(x, y)


class vector(collections.Sequence):

    PRECISION = 6

    __slots__ = ('_x', '_y', '_hash')

    def __init__(Self, x, y):

        Self._hash = None
        Self._x = round(x, Self.PRECISION)
        Self._y = round(y, Self.PRECISION)

    @property
    def x(Self):

        return Self._x

    @x.setter
    def x(Self, Value):
        if Self._hash is not None:
            raise ValueError('set x cannot be set after hashing')
        Self._x = round(Value, Self.PRECISION)

    @property
    def y(Self):

        return Self._y

    @y.setter
    def y(Self, Value):
        if Self._hash is not None:
            raise ValueError(' set y cannot be set after hashing')
        Self._y = round(Value, Self.PRECISION)

    def __hash__(Self):

        if Self._hash is None:
            pair = (Self.x, Self.y)
            Self._hash = hash(pair)
        return Self._hash

    def __len__(Self):

        return 2

    def __getitem__(Self, index):

        if index == 0:
            return Self.x
        if index == 1:
            return Self.y
        raise IndexError

    def copy(Self):

        type_Self = type(Self)
        return type_Self(Self.x, Self.y)

    def __eq__(Self, other):

        if isinstance(other, vector):
            return Self.x == other.x and Self.y == other.y
        return NotImplemented

    def __ne__(Self, other):

        if isinstance(other, vector):
            return Self.x != other.x or Self.y != other.y
        return NotImplemented

    def __iadd__(Self, other):

        if Self._hash is not None:
            raise ValueError('addition of vector cannot after hashing')
        elif isinstance(other, vector):
            Self.x += other.x
            Self.y += other.y
        else:
            Self.x += other
            Self.y += other
        return Self

    def __add__(Self, other):

        copy = Self.copy()
        return copy.__iadd__(other)

    __radd__ = __add__

    def move(Self, other):

        Self.__iadd__(other)

    def __isub__(Self, other):

        if Self._hash is not None:
            raise ValueError('subtraction of  vector cannot  happen after hashing')
        elif isinstance(other, vector):
            Self.x -= other.x
            Self.y -= other.y
        else:
            Self.x -= other
            Self.y -= other
        return Self

    def __sub__(Self, other):

        copy = Self.copy()
        return copy.__isub__(other)

    def __imul__(Self, other):

        if Self._hash is not None:
            raise ValueError(' multiplication of vector cannot happen  after hashing')
        elif isinstance(other, vector):
            Self.x *= other.x
            Self.y *= other.y
        else:
            Self.x *= other
            Self.y *= other
        return Self

    def __mul__(Self, other):

        copy = Self.copy()
        return copy.__imul__(other)

    __rmul__ = __mul__

    def scale(Self, other):

        Self.__imul__(other)

    def __itruediv__(Self, other):

        if Self._hash is not None:
            raise ValueError(' division of  vector cannot happen after hashing')
        elif isinstance(other, vector):
            Self.x /= other.x
            Self.y /= other.y
        else:
            Self.x /= other
            Self.y /= other
        return Self

    def __truediv__(Self, other):

        copy = Self.copy()
        return copy.__itruediv__(other)

    def __neg__(Self):

        copy = Self.copy()
        copy.x = -copy.x
        copy.y = -copy.y
        return copy

    def __abs__(Self):

        return (Self.x ** 2 + Self.y ** 2) ** 0.5



    def __repr__(Self):

        type_Self = type(Self)
        name = type_Self.__name__
        return '{}({!r}, {!r})'.format(name, Self.x, Self.y)
