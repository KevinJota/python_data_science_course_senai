import matplotlib.pyplot as plt

dados = [ 7, 8, 5, 6, 7, 8, 9, 5, 6, 7, 10, 10, 9, 6]

plt.hist(dados, bin=5, edgecolor="black", color="purple")
plt.title("Histograma Pyplot")
plt.xlabel("X label")
plt.ylabel("Y label")



plt.show()






