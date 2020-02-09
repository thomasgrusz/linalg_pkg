# For running unit tests, use
# /usr/bin/python -m unittest test_vector

import unittest

from linalg.vector import Vector


class TestVectorClass(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector([8.218, -9.341])
        self.v2 = Vector([-1.129, 2.111])
        self.v3 = Vector([8.218, -9.341])
        self.scalar = 7.41
        self.added = self.v1 + self.v2
        self.subtracted = self.v1 - self.v2
        self.multiplied = self.v1 * self.v2
        self.scalar_multiplied = self.v1 * 7.41

    def test_initialization(self):
        self.assertEqual(self.v1.coordinates, (8.218, -9.341), "incorrect coordinates")
        self.assertEqual(self.v1.dimension, 2, "incorrect dimension")

    def test_add(self):
        self.assertEqual(self.added.coordinates, (7.089, -7.23), "incorrect summation")

    def test_subract(self):
        self.assertEqual(
            self.subtracted.coordinates, (9.347, -11.452), "incorrect subtraction"
        )

    def test_multiply(self):
        self.assertEqual(
            self.multiplied.coordinates, (-9.278, -19.719), "incorrect subtraction"
        )

    def test_scalarmultiply(self):
        self.assertEqual(
            self.scalar_multiplied.coordinates,
            (60.895, -69.217),
            "incorrect subtraction",
        )

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 12.441, "incorrect magnitude")

    def test_normalized(self):
        self.assertEqual(
            self.v1.normalized().coordinates, (0.661, -0.751), "incorrect unit vector"
        )

    def test_repr(self):
        self.assertEqual(
            self.v1.__repr__(), "Vector: (8.218, -9.341)", "incorrect string"
        )

    def test_equal(self):
        self.assertEqual(self.v1.__eq__(self.v3), True, "vectors are not equal")
