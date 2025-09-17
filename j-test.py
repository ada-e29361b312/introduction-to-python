import numpy as np
import numpy.linalg as nply



from scipy.sparse import diags

n = 10

vals = np.array([-np.ones(n-1), 2*np.ones(n), -np.ones(n-1)]) #/ dx**2
A = diags(vals, [-1, 0, 1])

print(vals)
print(A.toarray())