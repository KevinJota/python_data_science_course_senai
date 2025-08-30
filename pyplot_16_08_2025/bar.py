import matplotlib.pyplot as plt

category = ['A','B','C','D','E']
values_month = [26, 45, 14, 8, 4]
values_last_month = [20, 20, 4, 7, 3]
maior = max(values_month)
index = 0

print(f'este é o maior no momento {maior}\f')

for a in values_month:
          if maior == a:
                    index = values_month.index(a)
                    print(f'achei! o index é: {index}')
                    break
         

plt.bar(category, values_month)
plt.bar(category, values_last_month)
# plt.grid(True)
plt.title("Vendas julho")
plt.xlabel("Categoria")
plt.ylabel("Valor do mês")
plt.ylim(0, 50)
plt.legend(['Qte.'], loc='best')
plt.text(category[index], maior, "AQUI!")
print(plt.axis())
plt.style.use("seaborn-v0_8-notebook")





plt.show()