from __future__ import division
import numpy as np


def test_as_nparrays():
    two_as_array = np.array([2])
    eight_as_array = np.array([8])
    assert(two_as_array[0] / eight_as_array[0] == 0.25)

