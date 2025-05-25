# iniciando projeto
def calcular(n1, n2, operacao):
    # Verifica tamanho das entradas
    if len(n1) != 8 or len(n2) != 8:
        raise Exception("tamanho da entrada invalido")

    # Verifica se todos os caracteres são '0' ou '1'
    for c in n1 + n2:
        if c != '0' and c != '1':
            raise Exception("valor invalido")

    # Verifica se a operação é válida
    if operacao not in ['+', '-', 'x']:
        raise Exception("valor invalido")

    # Soma binária sem converter para inteiro
    def soma_binaria(a, b):
        resultado = ['0'] * 8
        carry = '0'

        for i in range(7, -1, -1):
            bit1 = a[i]
            bit2 = b[i]

            # Soma dos bits (sem converter)
            total = 0
            if bit1 == '1':
                total += 1
            if bit2 == '1':
                total += 1
            if carry == '1':
                total += 1

            # Define resultado e novo carry
            if total % 2 == 0:
                resultado[i] = '0'
            else:
                resultado[i] = '1'

            carry = '1' if total >= 2 else '0'

        if carry == '1':
            raise Exception("overflow")

        return ''.join(resultado)

    # Inverte bits: '0' -> '1' e '1' -> '0'
    def inverter(bits):
        return ''.join('1' if b == '0' else '0' for b in bits)

    # Soma 1 ao binário, usando soma_binaria
    def mais_um(bits):
        return soma_binaria(bits, '00000001')

    # Subtração: usa complemento de 2
    def subtrair_binario(a, b):
        b_invertido = inverter(b)
        b_complemento2 = mais_um(b_invertido)
        return soma_binaria(a, b_complemento2)

    # Multiplicação binária sem conversão
    def multiplicar_binario(a, b):
        resultado = '00000000'
        for i in range(7, -1, -1):
            if b[i] == '1':
                # Desloca 'a' para esquerda (equivale a multiplicar por 2^posição)
                deslocamento = 7 - i
                parcial = a + '0' * deslocamento
                parcial = parcial[-8:]  # Mantém 8 bits
                resultado = soma_binaria(resultado, parcial)
        return resultado

    # Executa a operação
    if operacao == '+':
        return soma_binaria(n1, n2)
    elif operacao == '-':
        return subtrair_binario(n1, n2)
    elif operacao == 'x':
        return multiplicar_binario(n1, n2)

    try:
        n1 = input("Digite o primeiro número binário (8 bits): ")
        n2 = input("Digite o segundo número binário (8 bits): ")
        operacao = input("Digite a operação (+, -, x): ")

        resultado = calcular(n1, n2, operacao)
        print(f"Resultado: {resultado}")

    except Exception as e:
        print("Erro:", str(e))