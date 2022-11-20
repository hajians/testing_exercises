from testing_exercises.some_functions.square import square
import numpy as np


def test_square():
    # Given
    a = 2.0
    expected = 4.0

    # When
    output = square(a=a)

    # Then
    # Check if output == 4.0
    assert np.isclose(expected, output)
