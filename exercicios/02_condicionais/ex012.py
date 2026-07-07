# exercício 012 - média de notas

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media_notas = (nota1 + nota2) / 2

if media_notas <= 5:
    print(f'Reprovado. Média: {media_notas:.2f}')
elif media_notas <= 6.9:
    print(f'Recuperação. Média: {media_notas:.2f}')
else:
    print(f'Aprovado. Média: {media_notas:.2f}')