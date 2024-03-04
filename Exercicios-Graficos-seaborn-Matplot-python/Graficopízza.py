
import matplotlib.pyplot as plt

# Dados (cotações diárias das ações)
dias = list(range(1, 13))

vale5 = [82.2, 79.2, 84.0, 86.4, 84.8, 87.2, 88.8, 92.0, 89.6, 92.8, 95.2, 93.6]
unip6 = [75.0, 73.2, 75.6, 77.4, 78.2, 76.8, 78.0, 81.0, 82.2, 83.6, 83.4, 82.2]
bbas3 = [28.3, 27.9, 28.5, 29.2, 29.0, 29.4, 29.7, 30.1, 29.8, 30.2, 30.5, 30.3]


fiff,ax = plt.subplots()
ax.plot(dias, vale5)
ax.plot(dias, unip6)
ax.plot(dias, bbas3)

plt.xlabel("DIA")
plt.ylabel("PREÇOS R$")
plt.legend("Grafico Variado")


plt.show()