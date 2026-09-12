# Week 2

def mod_q(x, q):
    return x % q

def centered_mod(x, q):
    r = x % q
    if r > q // 2:
        r -= q
    return r
    
def poly_add(a, b, q):
    result = []

    for x, y in zip(a, b):
        result.append(mod_q(x + y, q))
        
    return result

def negacyclic_mul(a, b, q):
    listt = [a[0] * b[0], a[0] * b[1] + a[1] * b[0], a[1] * b[1]]
    listt[2] *= -1
    result = [listt[0] + listt[2], listt[1]]

    for i in range(len(result)):
        result[i] = mod_q(result[i], q)

    return result

def negacyclic_mul_generative(a, b, q):
    n = len(a)

    full = [0] * (2*n - 1) 
    for i in range(n):
        for j in range(n):
            full[i + j] += a[i] * b[j]

    result = [0] * n
    for k in range(2*n - 1):
        if k < n:
            result[k] += full[k]
        else:
            result[k - n] -= full[k]
    
    for i in range(n):
        result[i] = mod_q(result[i], q)

    return result

# Week 3

polynomial = [1, 2] # one polynomial
polynomial_vector = [[1, 2], [3, 4]] # vecor of polynomials
polynomial_matrix = [[[1, 2], [3, 4], [5, 6]], # matrix of polynomials
                     [[7, 8], [9, 10], [11, 12]],
                     [[13, 14], [15, 16], [17, 18]]]

class P:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __len__(self):
        return len(self.coeffs)
    
    def __repr__(self):
        if(len(self.coeffs) > 0):
            return f"Polynomial: {self.coeffs}"
        else:
            return "Polynomial is empty"

class P_V:
    def __init__(self, pols):
        self.pols = pols

    def __len__(self):
        return len(self.pols)
    
    def __repr__(self):
        result = ""

        for i in range(len(self.pols) - 1):
            result += str(self.pols[i].coeffs) + ", "

        if(len(self.pols) > 0):
            return "Vector of polynomials: " + result + str(self.pols[len(self.pols) - 1].coeffs)
        else:
            return "Vector is empty" 

class P_M:
    def __init__(self, vecs):
        self.vecs = vecs

    def __len__(self):
            return len(self.vecs)
    
    def __repr__(self):
        result = ""

        for i in range(len(self.vecs) - 1):
            coeffs_row = [p.coeffs for p in self.vecs[i].pols] # list of polynomials in one row
            result += str(coeffs_row) + ",\n"

        if(len(self.vecs) > 0):
            coeffs_row = [p.coeffs for p in self.vecs[len(self.vecs) - 1].pols]
            return "Matrix of polynomials:\n" + result + str(coeffs_row)
        else:
            return "Matrix is empty" 

def matrix_vector_mult(a, b, q): # a - matrix, b - vector
    la = len(a)
    lb = len(b) # ?
    n = len(b.pols[0].coeffs)
    result_pols = []

    for i in range(la):
        row_sum = [0] * n
        for j in range(lb):
            a_ij = a.vecs[i].pols[j].coeffs
            b_j = b.pols[j].coeffs
            prod = negacyclic_mul(a_ij, b_j, q)
            row_sum = poly_add(row_sum, prod, q)
        result_pols.append(P(row_sum))

    return P_V(result_pols)