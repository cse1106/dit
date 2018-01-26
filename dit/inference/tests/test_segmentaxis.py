"""
Tests for dit.inference.segmentaxis.
"""

import numpy as np

from dit.inference.segmentaxis import segment_axis


def test_sa1():
    """
    Test 2d.
    """
    a = np.arange(9).reshape(3, 3)
    sa = segment_axis(a, 2, 1)
    sa_correct = np.array([[0, 1],
                           [1, 2],
                           [2, 3],
                           [3, 4],
                           [4, 5],
                           [5, 6],
                           [6, 7],
                           [7, 8]])
    assert np.all(sa == sa_correct)


def test_sa2():
    """
    Test padding.
    """
    a = np.arange(5)
    sa = segment_axis(a, 2, 0, end='pad', endvalue=7)
    sa_correct = np.array([[0, 1],
                           [2, 3],
                           [4, 7]])
    assert np.all(sa == sa_correct)


def test_sa3():
    """
    Test cutting.
    """
    a = np.arange(5)
    sa = segment_axis(a, 2, 0, end='cut')
    sa_correct = np.array([[0, 1],
                           [2, 3]])
    assert np.all(sa == sa_correct)


def test_sa4():
    """
    Test wrapping.
    """
    a = np.arange(5)
    sa = segment_axis(a, 2, 0, end='wrap')
    sa_correct = np.array([[0, 1],
                           [2, 3],
                           [4, 0]])
    assert np.all(sa == sa_correct)
