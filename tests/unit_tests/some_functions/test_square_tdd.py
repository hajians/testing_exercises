import pytest

from testing_exercises.some_functions.square_tdd import square


def test_square_check_input():
    # Given
    a = True

    # When, Then
    with pytest.raises(TypeError):
        square(a=a)
