from math import sqrt


class Vector(object):
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

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(
                [
                    round(c1 * c2, 3)
                    for c1, c2 in zip(self.coordinates, other.coordinates)
                ]
            )
        else:
            return Vector([round(c * other, 3) for c in self.coordinates])

    def magnitude(self):
        sum_of_squares = sum([c ** 2 for c in self.coordinates])
        return round(sqrt(sum_of_squares), 3)

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self * (1.0 / magnitude)

        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")

    def __repr__(self):
        return f"Vector: {self.coordinates}"

    def __eq__(self, v):
        return self.coordinates == v.coordinates

