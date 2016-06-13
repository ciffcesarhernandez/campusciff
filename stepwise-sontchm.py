
# coding: utf-8

# In[1]:

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

# Importación de los datos
wine = pd.read_csv('winequality-white.csv', sep = ';')

# Separación de la variable objetivo y las explicativas
target = 'quality'
features = list(wine.columns)
features.remove('quality')

x = wine[features]
y = wine[target]

# Obtencion del conjunto de datos para validación
x_train, x_test, y_train, y_test = train_test_split(x, y)


# In[3]:

from sklearn.linear_model import LinearRegression

# Modelo para realizar los ajustes
model = LinearRegression()

# Variable para almecena los índices de la lista de atributos usados
feature_order = []
feature_error = []

# Iteración sobre todas las variables menos la una (importante para evitar
# que se intente hacer un modelo con ninguna variable en el último paso)
for i in range(len(features) - 1):
    idx_try = [val for val in range(len(features)) if val not in feature_order]
    iter_error = []

    for i_try in idx_try:
        # Se usan todas las variables que no han sido eliminadas
        useRow = idx_try[:]
        # Se retira una para evaluar su efecto
        useRow.remove(i_try)
        
        use_train = x_train[x_train.columns[useRow]]
        use_test = x_test[x_train.columns[useRow]]

        model.fit(use_train, y_train)
        rmsError = numpy.linalg.norm((y_test - model.predict(use_test)), 2)/sqrt(len(y_test))
        iter_error.append(rmsError)
    
    pos_best = numpy.argmin(iter_error)
    feature_order.append(idx_try[pos_best])
    feature_error.append(iter_error[pos_best])

for i in range(len(features) - 1):
    print "En el paso", i, "se ha eliminado la variable", features[feature_order[i]], "con un error", feature_error[i]


# In[ ]:



