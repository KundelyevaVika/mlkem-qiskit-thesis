import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from practice import poly_add, negacyclic_mul, mod_q, centered_mod

def test_poly_add():
    assert poly_add([1,2], [3,4], 7) == [4,6]
    print("test_poly_add: OK")

def test_negacyclic_mul():
    assert negacyclic_mul([2,4], [1,3], 7) == [4,3]
    print("test_negacyclic_mul: OK")

def test_negacyclic_mul_generative():
    assert negacyclic_mul([2,3], [4,5], 7) == [0,1]
    print("test_negacyclic_mul_generative: OK")

test_poly_add()
test_negacyclic_mul()
test_negacyclic_mul_generative()