import numpy as np
        
data =  [[1, 0, 0, 1, 0, 1, 0 ,0 ,0],
         [0, 1, 0, 0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 1, 0, 0],
         [0, 0, 1, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 1, 0, 0, 0, 1]]
        
myArray = np.array(data)       

mean = np.mean(myArray, axis = 0)
std = np.std(myArray, axis = 0)
print(mean)
print("-----")
print(std)
print("------------")
Z = ((myArray-mean)/std)
print(Z)
print("------")
Zmean = np.mean(Z, axis = 0)
print(Zmean)
print("-------")
temp = Z[1] - Z[6]
sumsq = np.dot(temp.T, temp)
print(np.sqrt(sumsq))
