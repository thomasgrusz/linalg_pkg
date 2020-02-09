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
        return Vector([c1 + c2 for c1, c2 in zip(self.coordinates, other.coordinates)])

    def __sub__(self, other):
        return Vector([c1 - c2 for c1, c2 in zip(self.coordinates, other.coordinates)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(
                [c1 * c2 for c1, c2 in zip(self.coordinates, other.coordinates)]
            )
        else:
            return Vector([c * other for c in self.coordinates])

    def __repr__(self):
        return f"Vector: {self.coordinates}"

    def __eq__(self, v):
        return self.coordinates == v.coordinates

