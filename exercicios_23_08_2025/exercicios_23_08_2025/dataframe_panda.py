import pandas as pd
import matplotlib.pyplot as plt

alunos = {
          'nome': ['ana', 'ramon', 'thiago', 'matheus', 'joel'],
          'idade': [ 18, 20, 16, 17, 20],
          'nota': [ 20, 50, 70, 80, 20]
}
df_aluno = pd.DataFrame(alunos)

# isso aq vai exibir somente NOMES        
# print(df_aluno.nome)
df_aluno['situacao'] = None


for n in range(len(df_aluno)):

          if df_aluno.nota[n] >= 70:
                    print('aprovado!')
                    df_aluno.loc[n, 'situacao'] = 'Aprovado'
          else:
                    print('desaprovado')
                    df_aluno.loc[n, 'situacao'] = 'Desaprovado'

maior = max(df_aluno.nota)
menor = min(df_aluno.nota)
media_n = df_aluno["nota"].mean() #calcula a média
media_i = df_aluno["idade"].mean()

#nome_dataframe.head() irá pegar os primeiros items/linhas do df,
# é possivel definir o numero de itens puxados
print(df_aluno.head(2))

# puxa os itens do DataFrame pelo seu index
print(df_aluno.iloc[[0,4]])

#pega alguns valores dentro de um intervalo pelo index
print(df_aluno[0:2], 'atual')

#pega o utlimo item
print(df_aluno.tail())

print(f'A nota média geral dos alunos é de: {media_n}')
print(f'A Idade média geral dos alunos é de: {media_i}')
print(f'a Maior nota foi: {maior}')
print(f'a menor nota foi: {menor}')
print(df_aluno)


# GRÁFICO DE BARRA: Nota e nome dos Alunos
def grafico_barra_nota():
          plt.bar(df_aluno['nome'], df_aluno['nota'])
          plt.title("Boletim geral")
          plt.xlabel("Nome do Aluno")
          plt.ylabel("Nota do Aluno")
          plt.ylim(0, 100)
          plt.show()
# grafico_barra_nota()


#GRÁFICO DE LINHA: IDADE e nome dos Alunos
def grafico_linha_idade():
          plt.title("Idade dos Alunos")
          plt.xlabel("Nome de Aluno")
          plt.ylabel("Idade")      
          plt.grid(True)    
          plt.plot(df_aluno['nome'], df_aluno['idade'], color="green")
          plt.show()
# grafico_linha_idade()
