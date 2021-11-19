import socket
from math import factorial

porta = 5050
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', porta))

while True: ## Servidor escuta até ser interrompido pelo user
    message, addr = s.recvfrom(1024)
    array = message.decode('utf-8').split(';')

    if len(array) <= 1:
        print('Ocorreu um erro ao obter os dados !')
    else:
        servico = array[0]
        n1 = array[1]
    
        if len(array) == 3:
            n2 = array[2]

    ## SOMA
    if(servico == '1'):
        r = int(n1)+int(n2)

    ## MULTIPLICAÇÃO
    elif(servico == '2'):
        r = int(n1) * int(n2)

    ## FATORIAL
    elif(servico == '3'):
        r = factorial(int(n1))

    msg = str(r)

    s.sendto(msg.encode('utf-8'), addr)