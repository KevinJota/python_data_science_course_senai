# lista de exercicios 1 a 10

lista_somar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
maior = 0
menor = 999

for a in lista_somar:
          # print(a)
          total += a

          if maior < a:
                    maior = a
          if a < menor:
                    menor = a

media =  total / len(lista_somar)

print(f' este é menor numero da lista: {menor}')
print(f' este é MAIOR numero da lista: {maior}')
print(f'n/ o total da lista_somar é: {total}')
print(f' a média da lista é: {media}')









