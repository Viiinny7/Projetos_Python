palavra_secreta = "bonito"
chances = 5
letras_acertadas = ''
letras_atentadas = []
while True:
    if chances == 0:
        break
    letra_digitada = input('digite uma letra: ')

    if len(letra_digitada)>1:
        letra_digitada = input('Digite apenas uma letra: ')
        continue

    if letra_digitada in palavra_secreta:
        print('Parabens, voce acertou uma letra')
        letras_acertadas+= letra_digitada
        

    else:
        print('AAAA que pena, voce errou, esta letra não está na palavra secreta')
        chances -=1
        
     
    letras_atentadas.append(letra_digitada)

    palavra_formada= ''
    for x in palavra_secreta:
        if x in letras_acertadas:
            palavra_formada += x

        else:
            palavra_formada += "*"

    print(palavra_formada)
    print(f'voce já digitou as seguintes letras {letras_atentadas}')

    if palavra_formada == palavra_secreta:
        print('Parabens, voce acertou a palavra secreta')
        break

    else:
        print(f'continue tentando, voce ainda tem mais {chances}')

        



    





    