import matplotlib.pyplot as plt
# este é uma biblioteca python usada para criar gráficos e visualização de dados utilizando
# poucos comandos e de forma simples

import theme


def gerador_grafico():
          eixo_x_dias = [1,5, 10, 15, 20, 25, 30]
          eixo_y_max_temp = [28, 29, 25, 32, 34, 36, 31]
          eixo_y_min_temp = [21, 22, 17, 23, 23, 24, 20]
          
          
          # for a in range(theme.plt_theme):
          #           print(theme.plt_theme[a])
                    
          tema = int(input("Escolha o seu tema de grágico de 0 á 27:"))
          plt.style.use(theme.plt_theme[tema])
          

          # eixo X é a base
          # eixo y compoem as linhas váriaveis

          # puro textos intuitivos para melhor visualizacao do grafico
          plt.title("Temp. Máximas e Minimas")
          plt.xlabel("Dias")
          plt.ylabel("Temperatura")
          
          plt.grid(True) #isso aqui habilita uma grade de fundo no gráfico
          
          plt.plot(eixo_x_dias, eixo_y_max_temp, color="green") #plt.plot adiciona uma linha ao gráfico
          plt.plot(eixo_x_dias, eixo_y_min_temp, marker="o")
          
          plt.text(2, 8, "title", fontsize=12)
          
          plt.legend(["Temp máx", "Temp min"], loc="best")

          print(plt.axis())
          print('rodou ok')
          plt.savefig("testando_matplotlib") # salva o grágico como arquivo png
          # print(plt.style.available)       # exibe estilos de gráficos disponibilizados pelo PLOT
          plt.show()

gerador_grafico()




