while True:
    num = int(input('digite um valor'))
    if num < 0:
        break

    cont = 1  # problema aqui
    while cont != 10:
        cont += 1
        print(f'{num} X {cont} = {num * cont}')