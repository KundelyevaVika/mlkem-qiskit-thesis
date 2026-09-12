import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from practice import P, P_V, P_M, matrix_vector_mult

def get_coeffs(vec):
    return [p.coeffs for p in vec.pols]


def test_polynomial_creation():
    pol1 = P([1, 2])
    assert pol1.coeffs == [1, 2]
    print("tpolynomial_creation: OK")


def test_vector_creation():
    pol1 = P([1, 2])
    pol2 = P([3, 4])
    pol_v1 = P_V([pol1, pol2])
    assert get_coeffs(pol_v1) == [[1, 2], [3, 4]]
    print("test_vector_creation: OK")


def test_matrix_creation():
    pol1 = P([1, 2])
    pol2 = P([3, 4])
    pol3 = P([5, 6])
    pol_v1 = P_V([pol1, pol2])
    pol_v2 = P_V([pol2, pol3])
    pol_m = P_M([pol_v1, pol_v2])
    assert get_coeffs(pol_m.vecs[0]) == [[1, 2], [3, 4]]
    assert get_coeffs(pol_m.vecs[1]) == [[3, 4], [5, 6]]
    print("test_matrix_creation: OK")


def test_matrix_vector_mult():
    pol1 = P([1, 2])
    pol2 = P([3, 4])
    pol3 = P([5, 6])
    pol_v1 = P_V([pol1, pol2])
    pol_v2 = P_V([pol2, pol3])
    pol_m = P_M([pol_v1, pol_v2])

    q = 7
    result = matrix_vector_mult(pol_m, pol_v1, q)

    expected = [[4, 0], [0, 6]]
    assert get_coeffs(result) == expected
    print("test_matrix_vector_mult: OK")

test_polynomial_creation()
test_vector_creation()
test_matrix_creation()
test_matrix_vector_mult()