import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#### CRIANDO A BASE DE DADOS 
np.random.seed(42)
ages = np.random.randint(low= 15 , high=70, size= 40 )
print(ages)
labels = []
for age in ages:
    if age < 30 :
        labels.append(0)
    else:
        labels.append(1)
#random swap
for i in range (0, 3):

    r= np.random.randint(0 , len(labels)-1)
    if labels[r] == 0:
        labels[r] = 1
    else:
        labels[r]= 0 
plt.scatter(ages, labels, color = "blue")
# plt.show()
## PREDIÇÃO USANDO REGRESSÃO LINEAR 

model = LinearRegression()
model.fit(ages.reshape(-1,1),labels)

m = model.coef_[0]
b = model.intercept_
print(m,b)

plt.plot(ages,ages * m + b , color = "blue")
plt.scatter(ages , labels , color = "red")
plt.show()
