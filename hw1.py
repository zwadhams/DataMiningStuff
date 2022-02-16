import numpy as np
import matplotlib.pyplot as plt

d = np.array([['red', 'yes', 'north'], ['blue', 'no', 'south'],
               ['yellow', 'no', 'east'], ['yellow', 'no', 'west'],
               ['red', 'yes', 'north'], ['yellow', 'yes', 'north'],
               ['blue', 'no', 'west']])

print(d)

X2 = d[:,1]
countY = sum(X2 == 'yes')
countN = sum(X2 == 'no')

plt.bar(x = ('yes','no'), height = (countY, countN), color = ('blue', 'yellow'))
plt.show()

