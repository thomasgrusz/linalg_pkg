# For running unit tests, use
# /usr/bin/python -m unittest test_vector

import unittest

from linalg.vector import Vector


class TestVectorClass(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector([8.218, -9.341])
        self.v2 = Vector([-1.129, 2.111])
        self.v3 = self.v1

    def test_initialization(self):
        self.assertEqual(self.v1.coordinates, (8.218, -9.341), "incorrect coordinates")
        self.assertEqual(self.v1.dimension, 2, "incorrect dimension")

    def test_add(self):
        self.added = self.v1 + self.v2
        self.assertEqual(self.added.coordinates, (7.089, -7.23), "incorrect summation")

    def test_subract(self):
        self.subtracted = self.v1 - self.v2
        self.assertEqual(
            self.subtracted.coordinates, (9.347, -11.452), "incorrect subtraction"
        )

    def test_times_scalar(self):
        self.multiplied_with_scalar = self.v1.times_scalar(7.41)
        self.assertEqual(
            self.multiplied_with_scalar.coordinates,
            (60.895, -69.217),
            "incorrect subtraction",
        )

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 12.441, "incorrect magnitude")

    def test_normalized(self):
        self.assertEqual(
            self.v1.normalized().coordinates, (0.661, -0.751), "incorrect normalization"
        )

    def test_dot(self):
        self.assertEqual(self.v1.dot(self.v2), -28.997, "incorrect dot product")

    def test_angle_with(self):
        self.assertEqual(
            self.v1.angle_with(self.v2, rad=True), 2.913, "incorrect angle"
        )
        self.assertEqual(
            self.v1.angle_with(self.v2, rad=False), 166.906, "incorrect angle"
        )

    def test_str(self):
        self.assertEqual(
            self.v1.__str__(), "Vector: (8.218, -9.341)", "incorrect string"
        )

    def test_equal(self):
        self.assertEqual(self.v1.__eq__(self.v3), True, "vectors are not equal")
