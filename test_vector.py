# For running unit tests, use
# /usr/bin/python -m unittest test_vector

import unittest
from math import pi, sqrt
from decimal import Decimal, getcontext
from linalg.vector import Vector

# Set precision level for Decimals class
getcontext().prec = 30


class TestVectorClass(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector([8.218, -9.341])
        self.v2 = Vector([-1.129, 2.111])

    def tearDown(self):
        del self.v1
        del self.v2

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
            (
                Decimal("7.08899999999999996802557689080"),
                Decimal("-7.22999999999999909405801190587"),
            ),
            "incorrect summation",
        )

    def test_subract(self):
        self.subtracted = self.v1 - self.v2
        self.assertEqual(
            self.subtracted.coordinates,
            (
                Decimal("9.34699999999999997513100424840"),
                Decimal("-11.4519999999999995132782260043"),
            ),
            "incorrect subtraction",
        )

    def test_times_scalar(self):
        self.assertEqual(
            self.v1.times_scalar(7.41).coordinates,
            (
                Decimal("60.8953800000000009572431736160"),
                Decimal("-69.2168099999999961676167004043"),
            ),
            "incorrect subtraction",
        )

    def test_magnitude(self):
        self.assertEqual(
            self.v1.magnitude(),
            Decimal("12.4414550997863584511084615581"),
            "incorrect magnitude",
        )

    def test_normalized(self):
        normalized_coordinates = (
            Decimal("0.660533670224885303647492786689"),
            Decimal("-0.750796424138555996928631643652"),
        )
        self.assertEqual(
            self.v1.normalized().coordinates,
            normalized_coordinates,
            "incorrect normalization",
        )

    def test_dot(self):
        dot_product = Decimal("-28.9969730000000004851195001266")
        # dot_product = (Decimal(8.218) * Decimal(-1.129)) + (
        #     Decimal(-9.341) * Decimal(2.111)
        # )
        self.assertEqual(self.v1.dot(self.v2), dot_product, "incorrect dot product")

    def test_angle_with(self):
        angle_in_rads = 2.9111755112971576
        self.assertEqual(
            self.v1.angle_with(self.v2, rad=True), angle_in_rads, "incorrect angle"
        )
        angle_in_degrees = angle_in_rads * 180.0 / pi
        self.assertEqual(
            self.v1.angle_with(self.v2, rad=False), angle_in_degrees, "incorrect angle"
        )

    def test_is_zero(self):
        zero_vector = Vector([0, 0, 0])
        self.assertEqual(
            zero_vector.is_zero(), True, "incorrect, this is a zero vector"
        )
        self.assertEqual(
            self.v1.is_zero(), False, "incorrect, this is NOT a zero vector"
        )

    def test_is_orthogonal_to(self):
        self.assertEqual(
            self.v1.is_orthogonal_to(self.v2),
            False,
            "incorrect, these vectors are not orthogonal to each other",
        )
        v3 = Vector([-2.328, -7.284, -1.214])  # orthogonal to v4
        v4 = Vector([-1.821, 1.072, -2.94])
        self.assertEqual(
            v3.is_orthogonal_to(v4),
            True,
            "incorrect result, these vectors are orthogonal to each other",
        )

    def test_is_parallel_to(self):
        self.assertEqual(
            self.v1.is_parallel_to(self.v2),
            False,
            "incorrect, these vectors are NOT parallel to eaach other",
        )
        v5 = Vector([-7.579, -7.88])  # parallel to v6
        v6 = Vector([22.737, 23.64])
        self.assertEqual(
            v5.is_parallel_to(v6),
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

    def test_cross(self):
        # Test case with 2D-vector when 3D-vectors is expected
        cross_product1 = (
            Decimal("-0E-51"),
            Decimal("0E-51"),
            Decimal("6.8022090000000024155504263490"),
        )
        self.assertEqual(
            self.v1.cross(self.v2).coordinates, cross_product1, "incorrect crossvector"
        )
        # Normal case with 3D-vectors
        cross_product2 = (
            Decimal("-11.2045709999999977337168388658"),
            Decimal("-97.6094439999999908463337305875"),
            Decimal("-105.685161999999993914045148813"),
        )
        v7 = Vector([8.462, 7.893, -8.187])
        v8 = Vector([6.984, -5.975, 4.778])
        self.assertEqual(
            v7.cross(v8).coordinates, cross_product2, "incorrect cross vector"
        )
        # Catch an expected error message if vector is 1D or > 3D
        v9 = Vector([1])
        with self.assertRaises(Exception):
            v9.cross(v9)

    def test_area_of_parallelogram_with(self):
        v7 = Vector([8.462, 7.893, -8.187])
        v8 = Vector([6.984, -5.975, 4.778])
        magnitude_of_cross_product = Decimal("144.300032696633225246124302074")
        self.assertEqual(
            v7.area_of_parallelogram_with(v8),
            magnitude_of_cross_product,
            "incorrect area of parallelogram",
        )

    def test_area_of_triangle_with(self):
        v7 = Vector([8.462, 7.893, -8.187])
        v8 = Vector([6.984, -5.975, 4.778])
        area_of_triangle = Decimal("144.300032696633225246124302074") / Decimal("2.0")
        self.assertEqual(
            v7.area_of_triangle_with(v8),
            area_of_triangle,
            "incorrect area of triangle",
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
        self.assertEqual(self.v1.__eq__(self.v1), True, "vectors are not equal")


if __name__ == "__main__":
    unittest.main()
