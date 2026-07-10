# exercício 006 - Progressão Aritmética (PA)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
quantidade_termos = int(input('Digite a quantidade de termos: '))


for contador in range(1, quantidade_termos + 1): 
    termo_atual = primeiro_termo + (contador - 1 ) * razao

    print(termo_atual, end=" ")