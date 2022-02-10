import numpy as np
import matplotlib.pyplot as plt

d = np.matrix([['red', 'yes', 'north'], ['blue', 'no', 'south'],
               ['yellow', 'no', 'east'], ['yellow', 'no', 'west'],
               ['red', 'yes', 'north'], ['yellow', 'yes', 'north'],
               ['blue', 'no', 'west']])

print(d)


plt.bar(x = 0, height = 5, data = d)

plt.show()
