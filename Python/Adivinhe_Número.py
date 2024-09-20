import random

def adivinhe_o_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break

adivinhe_o_numero()
