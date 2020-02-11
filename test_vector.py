# For running unit tests, use
# /usr/bin/python -m unittest test_vector

import unittest
from math import pi, sqrt
from decimal import Decimal, getcontext
from linalg.vector import Vector

getcontext().prec = 30


class TestVectorClass(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector([8.218, -9.341])
        self.v2 = Vector([-1.129, 2.111])
        self.v3 = Vector([8.218, -9.341])
        self.v4 = Vector([-2.328, -7.284, -1.214])  # orthogonal to v5
        self.v5 = Vector([-1.821, 1.072, -2.94])
        self.v6 = Vector([-7.579, -7.88])  # parallel to v7
        self.v7 = Vector([22.737, 23.64])

    def test_initialization(self):
        self.assertEqual(
            self.v1.coordinates,
            (Decimal(8.218), Decimal(-9.341)),
            "incorrect coordinates",
        )
        self.assertEqual(self.v1.dimension, 2, "incorrect dimension")

    def test_add(self):
        self.added = self.v1 + self.v2
        self.assertEqual(
            self.added.coordinates,
            ((Decimal(8.218) + Decimal(-1.129)), (Decimal(-9.341) + Decimal(2.111))),
            "incorrect summation",
        )

    def test_subract(self):
        self.subtracted = self.v1 - self.v2
        self.assertEqual(
            self.subtracted.coordinates,
            ((Decimal(8.218) - Decimal(-1.129)), (Decimal(-9.341) - Decimal(2.111))),
            "incorrect subtraction",
        )

    def test_times_scalar(self):
        self.multiplied_with_scalar = self.v1.times_scalar(7.41)
        self.assertEqual(
            self.multiplied_with_scalar.coordinates,
            ((Decimal(8.218) * Decimal(7.41)), (Decimal(-9.341) * Decimal(7.41))),
            "incorrect subtraction",
        )

    def test_magnitude(self):
        self.assertEqual(
            self.v1.magnitude(),
            ((Decimal(8.218) ** 2) + (Decimal(-9.341) ** 2)) ** Decimal(0.5),
            "incorrect magnitude",
        )

    def test_normalized(self):
        magnitude = ((Decimal(8.218) ** 2) + (Decimal(-9.341) ** 2)) ** Decimal(0.5)
        scalar = Decimal(1.0) / magnitude

        normalized_coordinates = ((Decimal(8.218) * scalar), (Decimal(-9.341) * scalar))
        self.assertEqual(
            self.v1.normalized().coordinates,
            normalized_coordinates,
            "incorrect normalization",
        )

    def test_dot(self):
        dot_product = (Decimal(8.218) * Decimal(-1.129)) + (
            Decimal(-9.341) * Decimal(2.111)
        )
        self.assertEqual(self.v1.dot(self.v2), dot_product, "incorrect dot product")

    def test_angle_with(self):

        angle_in_rads = 2.9111755112971575698566084611229598522186279296875
        angle_in_degrees = angle_in_rads * 180.0 / pi

        self.assertEqual(
            self.v1.angle_with(self.v2, rad=True), angle_in_rads, "incorrect angle"
        )
        self.assertEqual(
            self.v1.angle_with(self.v2, rad=False), angle_in_degrees, "incorrect angle"
        )

    def test_is_zero(self):
        self.zero_vector = Vector([0, 0, 0])
        self.assertEqual(
            self.zero_vector.is_zero(), True, "incorrect, this is a zero vector"
        )
        self.assertEqual(
            self.v1.is_zero(), False, "incorrect, this is NOT a zero vector"
        )

    def test_is_orthogonal_to(self):
        self.assertEqual(
            self.v4.is_orthogonal_to(self.v5),
            True,
            "incorrect result, these vectors are orthogonal to each other",
        )
        self.assertEqual(
            self.v1.is_orthogonal_to(self.v2),
            False,
            "incorrect, these vectors are not orthogonal to each other",
        )

    def test_is_parallel_to(self):
        self.assertEqual(
            self.v1.is_parallel_to(self.v2),
            False,
            "incorrect, these vectors are NOT parallel to eaach other",
        )
        self.assertEqual(
            self.v6.is_parallel_to(self.v7),
            True,
            "incorrect, these vectors are parallel to each other",
        )

    def test_component_parallel_to(self):
        coordinates = (
            Decimal("5.71240614001628270254847253295"),
            Decimal("-10.6810357498444410491684908966"),
        )
        self.assertEqual(
            self.v1.component_parallel_to(self.v2).coordinates,
            coordinates,
            "incorrect parallel component vector",
        )

    def test_component_orthogonal_to(self):
        coordinates = (
            Decimal("2.50559385998371726902981803665"),
            Decimal("1.34003574984444174550037194150"),
        )
        self.assertEqual(
            self.v1.component_orthogonal_to(self.v2).coordinates,
            coordinates,
            "incorrect orthogonal component vector",
        )

    def test_repr(self):
        self.assertEqual(
            self.v1.__repr__(),
            "Vector: (Decimal('8.217999999999999971578290569595992565155029296875'), Decimal('-9.3409999999999993036681189551018178462982177734375'))",
            "incorrect string representation",
        )

    def test_str(self):
        self.assertEqual(
            self.v1.__str__(), "Vector: [8.218, -9.341]", "incorrect string"
        )

    def test_equal(self):
        self.assertEqual(self.v1.__eq__(self.v3), True, "vectors are not equal")
