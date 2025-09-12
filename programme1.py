from matplotlib import pyplot as plt
import numpy as np

cars = ['BMW','Maruti Suzuki','BYD','Ferrari','Mercadies']

data = [98,66,12,54,9]

plt.pie(data,labels=cars)
plt.show()