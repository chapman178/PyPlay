import numpy as np
import matplotlib.pyplot as plt

# plt.plot([1,2],[1,2])


plt.show()
A1 = np.array(((1,2,10),(6,7,8)))
print('A1 is ',A1)
print(dir(A1))
print('transpose A1 : ',A1.T)
print('all A1 : ',A1.all)
print('data :',A1.data)

print('all :',A1.all())
print(A1.max(0))
print('std : ',A1.std(0))
print('flat :',A1.flat[:])