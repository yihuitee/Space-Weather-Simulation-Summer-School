#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Qusai Al Shidi'
__email__ = 'qusai@umich.edu'

from math import factorial
from math import pi


def cos_approx(x, accuracy=10):
    """Returns an approximate cosine using Taylor series.

    Args:
        x (float):
            To evaluate cosine of.
        accuracy (int):
            (default: 10) Number of Taylor series coefficients to use.

    Returns:
        (float): Approximate cosine of *x*.

    Examples:
        from math import pi
        cos_approx(pi)
        cos_approx(pi, accuracy=50)
    """

    def coeff(n):
        """Returns Taylor series coefficient of cosine"""
        return (-1)**n / factorial(2*n)

    series = [coeff(n) * x**(2*n) for n in range(accuracy)]
    return sum(series)



# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    print("cos(0) = ", cos_approx(0))
    print("cos(pi) = ", cos_approx(pi))
    print("cos(2*pi) = ", cos_approx(2*pi))
    print("more accurate cos(2*pi) = ", cos_approx(2*pi, accuracy=50))
