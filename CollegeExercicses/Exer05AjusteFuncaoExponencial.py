import numpy as np
from scipy.stats import linregress

# Dados fornecidos
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([8.03, 3.01, 1.10, 0.40, 0.15, 0.05])

# Aplicar o logaritmo natural nos valores de y
log_y = np.log(y)

# Realizar a regressão linear para encontrar os parâmetros ln(a) e b
slope, intercept, r_value, p_value, std_err = linregress(x, log_y)

# Calcular o valor de a (exponencial da interceptação)
a = np.exp(intercept)

# Determinar a função exponencial ajustada: y = a * e^(b * x)
# Calcular o valor de y para x = 2.5
x_new = 2.5
y_new = a * np.exp(slope * x_new)

# Exibir os parâmetros e o valor calculado para x = 2.5
print(f"Parâmetro a: {a}")
print(f"Parâmetro b (inclinação): {slope}")
print(f"Valor de y para x = 2.5: {y_new}")
