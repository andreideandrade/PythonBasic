if __name__ == '__main__':
    print("Atividade 01: ")

    # Declaração de variaveis
    saldo   = 1000
    salario = 4000
    despesas= 2967

    # Calculo sobre variaveis
    meta = saldo > 0 and salario - despesas >= 0.2 * salario

    # Mostra uma mensagem TRUE de acordo com a espressão acima
    print(meta)