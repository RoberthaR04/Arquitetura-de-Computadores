def calcular(n1, n2, operacao): #função que vai pegar o n1, n2 e operacao
    # Verifica tamanho dos bits
    if len(n1) != 8 or len(n2) != 8:
        #o raise serve para encaminhar esse alerta
        raise Exception("Tamanho da entrada invalido, por favor insira um valor com 8 numeros válidos")

    # Verifica se todos os caracteres são '0' ou '1', caso não, retorna uma mensagem para o usuário
    for c in n1 + n2:
        if c != '0' and c != '1':
            raise Exception("Valor invalido, por favor insira um valor que seja composto por 0 e 1")

    # Verifica se a operação é válida,  caso não, retorna uma mensagem para o usuário
    if operacao not in ['+', '-', 'x']:
        raise Exception("Operação inválida, insira uma operação válida")


    def soma_binaria(a, b): #função par afazer o cálculo
        resultado = ['0'] * 8 
        carry = '0' #caso sobre 1, vai colocar na próxima casa

        for i in range(7, -1, -1): #somando da direita pra esquerda
            bit1 = a[i] #pega cada bit na mesma posição 
            bit2 = b[i]

            total = 0 #serve pra contar quantos "1" terá, e o que sobra da última conta
            if bit1 == '1':
                total += 1
            if bit2 == '1':
                total += 1
            if carry == '1':
                total += 1
            #se o núemro fro ímpar, coloca 1. O número sendo par, adiciona 0
            resultado[i] = '1' if total % 2 else '0' 
            carry = '1' if total >= 2 else '0'
        #caso o número ultrapasse 8 bits, retorna um overflow
        if carry == '1':
            raise Exception("overflow")

        return ''.join(resultado) #reúne tudo e devolve a soma

    def inverter(bits): #troca os 0 por 1 e os 1 por 0
        return ''.join('1' if b == '0' else '0' for b in bits)

    def mais_um(bits): #sma 1 no número, sendo o complemento de 2
        return soma_binaria(bits, '00000001')

    def subtrair_binario(a, b): #na subtração, transforma o número subtraído em complemento de 2 e soma com outro
        b_invertido = inverter(b)
        b_complemento2 = mais_um(b_invertido)
        return soma_binaria(a, b_complemento2)

    def multiplicar_binario(a, b): #para multiplicar, começa com tudo zerado
        resultado = '00000000'
        for i in range(7, -1, -1): #percorre cada bit do segundo número.Se for 1 faz o cálculo
            if b[i] == '1':
                deslocamento = 7 - i #faz o deslocamento do número da esquerda
                parcial = a + '0' * deslocamento
                parcial = parcial[-8:]
                resultado = soma_binaria(resultado, parcial)
        return resultado #resultado final 
    #após o usuário escolher a operação, vai pra sua respectiva função
    if operacao == '+':
        return soma_binaria(n1, n2)
    elif operacao == '-':
        return subtrair_binario(n1, n2)
    elif operacao == 'x':
        return multiplicar_binario(n1, n2)

#Bloco interativo com input 
try:
    n1 = input("Digite o primeiro número binário (8 bits): ")
    n2 = input("Digite o segundo número binário (8 bits): ")
    operacao = input("Digite a operação (+, -, x): ")

    resultado = calcular(n1, n2, operacao)
    print(f"Resultado: {resultado}")
#serve para informar ao usuário que há algum erro
except Exception as e:
    print("Erro:", str(e))
