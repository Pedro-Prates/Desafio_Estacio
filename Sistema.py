import random

def mostrar_menu():
    print(f""""
                            Bem-Vindo {nome_jogador}!

        Este é o programa do Clyde. Escolha uma opção para ver o programa funcionar:

        Digite sua escolha:

        1- Jogue Pedra, Papel e Tesoura contra o Clyde;
        2- Faça o Clyde calcular seu IMC;
        3- Peça o Clyde para lhe dizer uma frase motivacional do dia;
        4- Dizer: "Tchau Clyde!" e sair.
        \n
        """)

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    clyde = opcoes[random.randint(0, 2)]
    jogador = input("Escolha: pedra, papel ou tesoura? ").lower()

    print(f"\n\nClyde escolheu {clyde}\n")

    if jogador == clyde:
        print(f"Empate!\nVem tranquilo {nome_jogador}.")
    elif (jogador == "pedra" and clyde == "tesoura") or (jogador == "papel" and clyde == "pedra") or (jogador == "tesoura" and clyde == "papel"):
        print(f"Você ganhou!\nNa cagada hein {nome_jogador}, da próxima eu ganho!")
    else:
        print(f"Você perdeu {nome_jogador}!\n\nEu sou o milior!\n\n\n")
    

def calcular_imc():
    peso = float(input("Digite seu peso em kg:"))
    altura = float(input("Digite sua altura em metros: "))

    IMC = peso / (altura ** 2)

    print(f"\n\n{nome_jogador} é o resultado do seu IMC: {IMC:.2f}\n\n\n")
    


def frase_do_dia():
    frases = ["Tudo passa, nem que seja por cima de você", "Não sabendo que era impossível, foi lá e soube", "A luta é grande e a derrota é certa"]
    aleatorio = random.randint(0, len(frases) -1)
    
    print(f'\n\nUsando toda sua sabedoria, Clyde disse: \n\n"{frases[aleatorio]}"\n\n\n')

nome_jogador = input("Digite seu nome: ")

while True:
    mostrar_menu()
    opcao = int(input(f"{nome_jogador} escolha uma opção: "))

    if opcao == 1:
        jogar()
    elif opcao == 2:
        calcular_imc()
    elif opcao == 3:
        frase_do_dia()
    elif opcao == 4:
        print("\nClyde queria ter jogado mais com você!\n")
        break
    else:
        print("Opção inválida!\nVocê é mais burro que o Clyde!!!")
