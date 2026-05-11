import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

column_names = ['Sex', 'Length', 'Diameter', 'Height', 'WholeWeight', 
                'ShuckedWeight', 'VisceraWeight', 'ShellWeight', 'Rings']

df = pd.read_csv('E:/University/Data Mining/Assignments/HW2/abalone/abalone.data', names=column_names)

df = df.drop('Sex', axis=1)

x = df.drop('Rings', axis=1)
y = df['Rings'] + 1.5

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

rmses = []

for k in range(1, 11):
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(x_train_scaled, y_train)
    y_pred = model.predict(x_test_scaled)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    rmses.append(rmse)

plt.figure()
plt.plot(range(1, 11), rmses, marker='o', linestyle='--', color='blue')
plt.title('RMSE per K values')
plt.xlabel('K values')
plt.ylabel('RMSE')
plt.grid(True)
plt.xticks(range(1, 11))
plt.show()
