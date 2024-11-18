import numpy as np
import matplotlib.pyplot as plt

# Задаємо функцію
x = np.linspace(0.01, 5, 500)  
y = 5 * np.cos(10 * x) * np.sin(3 * x) / (x ** 0.5)

# Створюємо графік
plt.figure(figsize=(10, 6))
plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label=r'$Y(x)=\frac{5\cos(10x)\sin(3x)}{\sqrt{x}}$')

# Оформлення графіка
plt.title("Графік функції Y(x)", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("Y(x)", fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# Виведення графіка
plt.show()