# -------------------------------------------
# 💰 SISTEMA BANCÁRIO SIMPLES (banco do cartiado)
# Feito em Python por Otávio Salton 
# -------------------------------------------

# Importa o módulo 'os' para verificar se o arquivo de contas existe no computador
import os

# ---- Códigos de cores para deixar o terminal colorido ----
VERDE = "\033[92m"      # Verde - mensagens de sucesso
VERMELHO = "\033[91m"   # Vermelho - mensagens de erro/alerta
AMARELO = "\033[93m"    # Amarelo - títulos e destaques
AZUL = "\033[94m"       # Azul - textos neutros
NEGRITO = "\033[1m"     # Negrito
RESET = "\033[0m"       # Reset - volta à cor normal

# Lista que vai armazenar todas as contas do sistema
# Cada conta será um DICIONÁRIO (com número, nome e saldo) 
contas = []

# Nome do arquivo onde os dados serão salvos
ARQUIVO_CONTAS = "contas.txt"


# --------------------------------------------------------------
# Função: salvar_contas_em_arquivo
# Objetivo: salvar todas as contas em um arquivo .txt
# --------------------------------------------------------------
def salvar_contas_em_arquivo():
    # Abre o arquivo no modo escrita ("w") — sobrescreve o conteúdo
    with open(ARQUIVO_CONTAS, "w") as arquivo:
        # Para cada conta na lista 'contas', grava uma linha com seus dados
        for conta in contas:
            linha = f"{conta['numero']};{conta['nome']};{conta['saldo']}\n"
            arquivo.write(linha)


# --------------------------------------------------------------
# Função: carregar_contas_do_arquivo
# Objetivo: ler as contas que já estão salvas no arquivo
# --------------------------------------------------------------
def carregar_contas_do_arquivo():
    # Verifica se o arquivo existe no computador
    if os.path.exists(ARQUIVO_CONTAS):
        with open(ARQUIVO_CONTAS, "r") as arquivo:
            for linha in arquivo:
                # Divide a linha pelos ';' e cria um dicionário para cada conta
                numero, nome, saldo = linha.strip().split(";")
                contas.append({
                    "numero": int(numero),
                    "nome": nome,
                    "saldo": float(saldo)
                })


# --------------------------------------------------------------
# Função: criar_conta
# Objetivo: cadastrar uma nova conta no sistema
# --------------------------------------------------------------
def criar_conta():
    # Solicita os dados do usuário
    numero = int(input(f"{AZUL}Número da conta: {RESET}"))
    nome = input(f"{AZUL}Nome do titular: {RESET}")

    # Verifica se o número já existe (não pode repetir)
    for conta in contas:
        if conta["numero"] == numero:
            print(f"{VERMELHO}⚠️ Conta já existente!{RESET}")
            return  # Sai da função

    # Cria um novo dicionário representando a conta
    nova_conta = {"numero": numero, "nome": nome, "saldo": 0.0}
    # Adiciona à lista de contas
    contas.append(nova_conta)
    # Salva no arquivo
    salvar_contas_em_arquivo()
    print(f"{VERDE}✅ Conta criada com sucesso!{RESET}")


# --------------------------------------------------------------
# Função: depositar
# Objetivo: adicionar dinheiro ao saldo de uma conta
# --------------------------------------------------------------
def depositar():
    numero = int(input(f"{AZUL}Número da conta: {RESET}"))
    valor = float(input(f"{AZUL}Valor do depósito: {RESET}"))

    # Procura a conta pelo número
    for conta in contas:
        if conta["numero"] == numero:
            conta["saldo"] += valor  # soma o depósito ao saldo
            salvar_contas_em_arquivo()  # salva a atualização
            print(f"{VERDE}💵 Depósito realizado com sucesso!{RESET}")
            return
    # Caso a conta não exista:
    print(f"{VERMELHO}⚠️ Conta não encontrada.{RESET}")


# --------------------------------------------------------------
# Função: sacar
# Objetivo: retirar dinheiro de uma conta, se houver saldo
# --------------------------------------------------------------
def sacar():
    numero = int(input(f"{AZUL}Número da conta: {RESET}"))
    valor = float(input(f"{AZUL}Valor do saque: {RESET}"))

    for conta in contas:
        if conta["numero"] == numero:
            # Verifica se há saldo suficiente
            if conta["saldo"] >= valor:
                conta["saldo"] -= valor
                salvar_contas_em_arquivo()
                print(f"{VERDE}💸 Saque realizado com sucesso!{RESET}")
            else:
                print(f"{VERMELHO}❌ Saldo insuficiente.{RESET}")
            return
    print(f"{VERMELHO}⚠️ Conta não encontrada.{RESET}")


# --------------------------------------------------------------
# Função: mostrar_saldo
# Objetivo: mostrar o saldo e o nome do titular da conta
# --------------------------------------------------------------
def mostrar_saldo():
    numero = int(input(f"{AZUL}Número da conta: {RESET}"))

    for conta in contas:
        if conta["numero"] == numero:
            print(f"\n{NEGRITO}👤 Titular:{RESET} {conta['nome']}")
            print(f"{NEGRITO}💰 Saldo atual:{RESET} R$ {conta['saldo']:.2f}\n")
            return
    print(f"{VERMELHO}⚠️ Conta não encontrada.{RESET}")


# --------------------------------------------------------------
# Função: listar_contas
# Objetivo: mostrar todas as contas cadastradas
# --------------------------------------------------------------
def listar_contas():
    print(f"\n{AMARELO}=== LISTA DE CONTAS CADASTRADAS ==={RESET}")
    for conta in contas:
        print(f"{AZUL}Número:{RESET} {conta['numero']} | "
              f"{AZUL}Titular:{RESET} {conta['nome']} | "
              f"{AZUL}Saldo:{RESET} R$ {conta['saldo']:.2f}")
    print(f"{AMARELO}====================================={RESET}\n")



    # Função: analise_financeira
# Objetivo: gerar um relatório completo dos valores do banco
# --------------------------------------------------------------
def analise_financeira():
    if not contas:
        print(f"{VERMELHO}⚠️ Nenhuma conta cadastrada para análise.{RESET}")
        return

    total = sum(conta["saldo"] for conta in contas)
    media = total / len(contas)

    # Conta com maior saldo
    conta_maior = max(contas, key=lambda c: c["saldo"])
    # Conta com menor saldo
    conta_menor = min(contas, key=lambda c: c["saldo"])

    print(f"\n{AMARELO}{NEGRITO}===== ANÁLISE FINANCEIRA DO BANCO ====={RESET}")
    print(f"{AZUL}Total de contas cadastradas:{RESET} {len(contas)}")
    print(f"{AZUL}Total armazenado no banco:{RESET} R$ {total:.2f}")
    print(f"{AZUL}Média de saldo por conta:{RESET} R$ {media:.2f}")

    print(f"\n{AZUL}Conta com MAIOR saldo:{RESET}")
    print(f"• Titular: {conta_maior['nome']}")
    print(f"• Número: {conta_maior['numero']}")
    print(f"• Saldo: R$ {conta_maior['saldo']:.2f}")

    print(f"\n{AZUL}Conta com MENOR saldo:{RESET}")
    print(f"• Titular: {conta_menor['nome']}")
    print(f"• Número: {conta_menor['numero']}")
    print(f"• Saldo: R$ {conta_menor['saldo']:.2f}")

    print(f"{AMARELO}==========================================={RESET}\n")


# --------------------------------------------------------------
# Função principal do programa
# --------------------------------------------------------------
def main():
    # Carrega as contas salvas no arquivo, se existirem
    carregar_contas_do_arquivo()

    # Laço principal do menu (roda até o usuário sair)
    while True:
        # Mostra o menu com opções
        print(f"\n{NEGRITO}{AMARELO}==== MENU PRINCIPAL ==== {RESET}")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Mostrar saldo")
        print("5 - Listar todas as contas")
        print("6 - Análise financeira do banco")
        print("0 - Sair")

        # Lê a opção escolhida
        opcao = input(f"{AZUL}Escolha uma opção: {RESET}")

        # Condicionais que definem o que o programa vai fazer
        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            mostrar_saldo()
        elif opcao == "5":
            listar_contas()
        elif opcao == "6":
            analise_financeira()
        elif opcao == "0":
            # Sai do laço e termina o programa
            print(f"{VERDE}Encerrando o sistema... 👋{RESET}")
            break
        else:
            print(f"{VERMELHO}❌ Opção inválida! Tente novamente.{RESET}")


            # --------------------------------------------------------------
# Função: analise_financeira
# Objetivo: gerar um relatório completo dos valores do banco
# --------------------------------------------------------------



# --------------------------------------------------------------
# Execução do programa
# --------------------------------------------------------------
# Essa parte garante que o programa só rode o menu
# quando for executado diretamente (e não importado como módulo)
if __name__ == "__main__":
    main()
