#%%
# Diagram Kartesius #
import matplotlib.pyplot as plt

x_axis = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_axis = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.title('Diagram Kartesius')
plt.scatter(x_axis, y_axis, color="red", marker='o', label='item 1')


plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.grid(True)
plt.legend()

plt.show()
# ===================== #
# %%
# GRAFIK GARIS #
y = [2990, 2710, 2540, 3300, 2990]
x = [18, 19, 20, 21, 22]
plt.plot(x, y)

plt.xlabel('Label X')
plt.ylabel('Label Y')

plt.title('Grafik Garis')
plt.grid(True)

plt.show()
# =================== #
# %%
# Gelombang Sinus #
import numpy as np

t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2.5 * np.pi * t)
plt.plot(t, s)

plt.xlabel('Label X')
plt.ylabel('Label Y')

plt.title('Gelombang Sinus')
plt.grid(True)

plt.show()
# ================== #
# %%
# Bar Chart #
from matplotlib import style

style.use('ggplot')

x = [0, 1, 2, 3, 4, 5]
y = [24.27, 23.18, 22.39, 8.41, 7.19, 6.62]

fig, ax = plt.subplots()

ax.bar(x, y, align='center')

ax.set_title('Bahasa Pemrograman Favorit (UMSU)')
ax.set_ylabel('Pengguna')
ax.set_xlabel('Bahasa')

ax.set_xticks(x)
ax.set_xticklabels(("Python", "JavaScript", "Java", "C#", "PHP", "C++"))

plt.show()
# ===================== #
# %%
# Pie Chart #
labels = ['Hijau', 'Kuning', 'Biru', 'Merah']
quantity = [3, 10, 12, 11]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

plt.title('Pie Chart')
plt.pie(quantity, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')
plt.show()
# ===================== #
# %%
