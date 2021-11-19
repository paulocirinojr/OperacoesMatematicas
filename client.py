from rpc import OperacoesMatematicas

RPC_SERVER = "localhost"
RPC_PORT = 5050

op = OperacoesMatematicas(RPC_SERVER, RPC_PORT)
service = input('Qual operação você deseja?\n1 - Adição\n2 - Multiplicação\n3 - Fatorial\nOpção desejada: ')

if (service == '1'):
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')
    result = op.soma(int(n1),int(n2))
    print('O resultado da soma é: ', result)

elif (service == '2'):
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')
    result = op.produto(int(n1),int(n2))
    print('O resultado da multiplicação é: ', result)

elif (service == '3'):
    n1 = input('Digite o número: ')
    result = op.fatorial(int(n1))
    print('O resultado do fatorial de '+n1+' é: ', result)