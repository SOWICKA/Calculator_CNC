# Importing necessary libraries for unit testing
import unittest
from unittest.mock import Mock, patch

# Since the original script is not structured in a way that easily allows for unit testing without significant refactoring,
# this mock-up will simulate the process of testing a simplified version of the calculation logic.
# This example will focus on the milling operation calculation logic, extracted and simplified for demonstration.

# Mocked function for demonstration purposes
def calculate_milling_parameters(vc, fi, z, fz):
    """
    Simplified calculation logic for milling operation.
    vc: Cutting speed in m/min
    fi: Tool diameter in mm
    z: Number of cutting teeth
    fz: Feed per tooth in mm
    Returns tuple of (spindle speed in RPM, feed rate in mm/min)
    """
    if vc <= 0 or fi <= 0 or z <= 0 or fz <= 0:
        raise ValueError("All parameters must be positive numbers.")

    pi = 3.1416
    spindle_speed = (vc * 1000) / (fi * pi)  # Calculate spindle speed in RPM
    feed_rate = spindle_speed * fz * z  # Calculate feed rate in mm/min

    return int(spindle_speed), int(feed_rate)

# Unit test class
class TestCNCMillingCalculations(unittest.TestCase):

    def test_calculate_milling_parameters_positive(self):
        """
        Test that the milling calculation returns correct spindle speed and feed rate
        with positive inputs.
        """
        vc, fi, z, fz = 100, 10, 4, 0.1  # Example input values
        expected_spindle_speed, expected_feed_rate = 3183, 1273  # Expected output values based on the input
        result = calculate_milling_parameters(vc, fi, z, fz)
        self.assertEqual(result, (expected_spindle_speed, expected_feed_rate))

    def test_calculate_milling_parameters_zero(self):
        """
        Test that the milling calculation raises a ValueError when any of the inputs are zero or negative.
        """
        with self.assertRaises(ValueError):
            calculate_milling_parameters(0, 10, 4, 0.1)  # Zero cutting speed

# Running the tests
unittest.main(argv=[''], exit=False)