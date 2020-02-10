from math import acos, degrees, pi, sqrt
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be non empty!")

        except TypeError:
            raise TypeError("The coordinates must be an iterable!")

    def __add__(self, v):
        return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    def times_scalar(self, c):
        return Vector([x * Decimal(c) for x in self.coordinates])

    def magnitude(self):
        sum_of_squares = sum([x ** 2 for x in self.coordinates])
        return (sum_of_squares) ** Decimal(0.5)

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal(1.0) / magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, rad=True):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_rads = acos(u1.dot(u2))
            if rad:
                return angle_in_rads
            else:
                return angle_in_rads * 180.0 / pi

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute an angle with the zero vector")
            else:
                raise e

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        return (
            self.is_zero()
            or v.is_zero()
            or self.angle_with(v) == 0
            or self.angle_with(v) == pi
        )

    def __repr__(self):
        coordinates = [round(float(x), 3) for x in self.coordinates]
        return f"Vector: {coordinates}"

    def __eq__(self, v):
        return self.coordinates == v.coordinates
