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

    ##############################
    ##      Atividade 4         ##
    ##############################
    #   Operadores usando variáveis

    x = 2
    y = 7
    z = 5
    print("X é maior que Z? -> ", x > z)
    print("Z é menor ou igual a y? -> ", z <= y)
    print("Y é diferente de X? -> ", y != x)
    print("==================================")
    ##############################
    ##      Atividade 4         ##
    ##############################
    #   Operadores usando condicionais

    print("Operadores usando condicionais")
    if 2 > 1:
        print('Usando numeros: 2 é maior que 1')

    num1 = 2
    num2 = 1
    if num1 > num2:
        print('Usando variaveis: 2 é maior que 1')

    ##############################
    ##      Atividade 4         ##
    ##############################
    #   Operadores de identidade
    print('Operadores de identidade')

    aluguel = 250
    energia = 250
    agua = 65
    print('Operador ( is ): ', aluguel is energia)