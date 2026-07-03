p1 = float(input('digite a primeira nota'))
p2 = float(input('digite a segunda nota'))
media = (p1 + p2) / 2
if media <= 5:
    print(f'reprovado media: {media}')
elif 5 <= media <= 6.9:
    print(f'recuperação media: {media}')
else:
    print(f'aprovado media: {media}')
