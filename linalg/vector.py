from math import acos, degrees, sqrt


class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be non empty!")

        except TypeError:
            raise TypeError("The coordinates must be an iterable!")

    def __add__(self, other):
        return Vector(
            [round(c1 + c2, 3) for c1, c2 in zip(self.coordinates, other.coordinates)]
        )

    def __sub__(self, other):
        return Vector(
            [round(c1 - c2, 3) for c1, c2 in zip(self.coordinates, other.coordinates)]
        )

    def times_scalar(self, other):
        return Vector([round(c * other, 3) for c in self.coordinates])

    def magnitude(self):
        sum_of_squares = sum([c ** 2 for c in self.coordinates])
        return round(sqrt(sum_of_squares), 3)

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1.0 / magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, other):
        dot_product_full = sum(
            [c1 * c2 for c1, c2 in zip(self.coordinates, other.coordinates)]
        )
        return round(dot_product_full, 3)

    def angle_with(self, other, rad=True):
        try:
            v1 = self.normalized()
            v2 = other.normalized()
            angle_rads = acos(v1.dot(v2))
            if rad:
                return round(angle_rads, 3)
            else:
                return round(degrees(angle_rads), 3)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute an angle with the zero vector")
            else:
                raise e

    def __str__(self):
        return f"Vector: {self.coordinates}"

    def __eq__(self, v):
        return self.coordinates == v.coordinates

