from math import acos, degrees, pi, sqrt
from decimal import Decimal, getcontext

# Set precision level for Decimals class
getcontext().prec = 30


class Vector(object):
    """Vector class for storing vectors and calculating basic vector operations
    
    Attributes:
        coordinates (Decimal)
        dimensions (int)
    
    Returns:
        Vector object -- an object with coordinates and number of dimentsions
    """

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector"
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = "No unique orthogonal component"
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = "No unique parallel component"
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = "Only defined in two or three dimensions"

    # Constructor for a Vector object
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

    # Add two vectors (operator overload)
    def __add__(self, v):
        return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])

    # Subtract two vectors (operator overload)
    def __sub__(self, v):
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    # Multiply a vector with a scalar
    def times_scalar(self, c):
        return Vector([x * Decimal(c) for x in self.coordinates])

    # Calculate the magnitude or length of a vector
    def magnitude(self):
        sum_of_squares = sum([x ** 2 for x in self.coordinates])
        return (sum_of_squares) ** Decimal(0.5)

    # Calculate the unit vector (normalization) of a vector
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal(1.0) / magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    # Calculate the Dot Product of two vectors
    def dot(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    # Calculate the angle between two vectors
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

    # Check if a vector has length (magnitude) of zero
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    # Check if two vectors are orthogonal (90°) to each other
    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    # Check if two vectors are parallel (0°) to each other
    def is_parallel_to(self, v):
        return (
            self.is_zero()
            or v.is_zero()
            or self.angle_with(v) == 0
            or self.angle_with(v) == pi
        )

    # Calculate the projection of a vector onto a basis (parallel component)
    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    # Calculate the orthogonal component of a vector
    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self - projection

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    # Calculate the cross product
    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [
                y_1 * z_2 - y_2 * z_1,
                -(x_1 * z_2 - x_2 * z_1),
                x_1 * y_2 - x_2 * y_1,
            ]
            return Vector(new_coordinates)

        except ValueError as e:
            msg = str(e)
            # If input vectors are 2D, then add another dimension and
            # calculate the cross product
            if msg == "not enough values to unpack (expected 3, got 2)":
                self_embedded_in_R3 = Vector(self.coordinates + ("0",))
                v_embedded_in_R3 = Vector(v.coordinates + ("0",))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (
                # If input vectors are 1D or 4D and above, raise an exception
                msg == "too many values to unpack (expected 3)"
                or msg == "not enough values to unpack (expected 3, got 1)"
            ):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    # Calculate the area of a parallelogram spanned by two vectors
    def area_of_parallelogram_with(self, v):
        cross_product = self.cross(v)
        return cross_product.magnitude()

    # Calculate the area of a triangle spanned by two vectors
    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / Decimal("2.0")

    # Define the inner representation of a Vector object
    def __repr__(self):
        return f"Vector: {self.coordinates}"

    # Define the string output format of a Vector object
    def __str__(self):
        coordinates = [round(float(x), 3) for x in self.coordinates]
        return f"Vector: {coordinates}"

    # Define the 'equals' (==) method
    def __eq__(self, v):
        return self.coordinates == v.coordinates
