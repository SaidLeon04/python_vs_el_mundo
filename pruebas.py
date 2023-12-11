import matplotlib.pyplot as plt
from datetime import datetime

# Datos
fechas = ['2023-11-17', '2023-11-21', '2023-11-23', '2023-11-25']
valores = [411.6, 516.3, 270, 321]

# Convertir fechas a formato datetime
fechas_dt = [datetime.strptime(fecha, '%Y-%m-%d') for fecha in fechas]

# Crear la gráfica
plt.figure(figsize=(8, 5))
plt.plot(fechas_dt, valores, marker='o', linestyle='-', color='b')
plt.title('Gráfico de fechas y valores')
plt.xlabel('Fechas')
plt.ylabel('Valores')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar la gráfica
plt.show()
