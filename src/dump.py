import numpy as np
X = np.matrix('1 2; 3 4')
eq = (X.transpose()*X).I
print eq