import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

datosT = [11050000, 22100000, 33150000, 44200000, 55250000]
searchN = [22100002, 44200002, 66300002, 88400002, 110500002]
delete = [5, 5, 5, 5, 5]

dato = np.array(datosT) / 1e6

fig, ax = plt.subplots(figsize=(8,5))
ax.plot(dato, searchN, marker='o', linestyle='-', label="delete()", color="#FF69B4")
ax.plot(dato, delete, marker='s', linestyle='-', label="search()", color="#DB7093")

ax.set_xlabel("Número de elementos en la pila (n)")
ax.set_ylabel("Recurrencias")
ax.set_title("Comparación de recurrencias de delete() y search() en un stack")

ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M'))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.1f}M'))

ax.legend()
ax.grid(True)

plt.show()