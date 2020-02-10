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
            sqrt((Decimal(8.218) ** 2) + (Decimal(-9.341) ** 2)),
            "incorrect magnitude",
        )

    def test_normalized(self):
        magnitude = Decimal(sqrt((Decimal(8.218) ** 2) + (Decimal(-9.341) ** 2)))
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

    def test_repr(self):
        self.assertEqual(
            self.v1.__repr__(), "Vector: [8.218, -9.341]", "incorrect string"
        )

    def test_equal(self):
        self.assertEqual(self.v1.__eq__(self.v3), True, "vectors are not equal")
