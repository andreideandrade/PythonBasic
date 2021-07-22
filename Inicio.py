if __name__ == '__main__':
    ##############################
    ##      Atividade 1         ##
    ##############################
    #   Operadores lógicos

    print("Atividade 01: ")

    # Declaração de variaveis
    saldo = 1000
    salario = 4000
    despesas = 2967

    # Calculo sobre variaveis
    meta = saldo > 0 and salario - despesas >= 0.2 * salario

    # Mostra uma mensagem TRUE de acordo com a espressão acima
    print(meta)

    ##############################
    ##      Atividade 2         ##
    ##############################
    #   Operadores de membro

    print("Atividade 02: Operadores de membro")

    lista = [1, 2, 3, 'Ana', 'Maria']

    # Procura o valor na lista e retorna TRUE se verdadeiro

    print("Numero 2 está na lista: ", 2 in lista)

    #   Operador de negação

    print("O nome Maria não está na lista: ", 'Maria' not in lista)

    ##############################
    ##      Atividade 3         ##
    ##############################
    #   Operadores relacionais

    print("3 é maior que 4? -> ", 3 > 4)

    print("7 é maior ou igual a 3? -> ", 7 >= 3)

    print("3 é maior ou igual a 3? -> ", 3 >= 3)
