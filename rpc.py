import socket

# Cria a conexão e envia os dados via socket
def criaConexao(self, dados):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(dados.encode('utf-8'), (self.ip, self.porta))
    msg, addr = s.recvfrom(1024) # Recebe a resposta do server
    s.close() # Fecha a conexão
    msg = msg.decode('utf-8') # Decodifica a mensagem e retorna o resultado
    return msg

class OperacoesMatematicas:
    # Inicializa a classe com o IP e Porta recebidos
    def __init__(self, ip, porta):
        self.ip = ip
        self.porta = porta

    ###

        # as 3 operações obtém os dados do cliente, enviam para o servidor em forma de string,
        # utilizando o separador ';', onde o primeiro caractere é o tipo de serviço, o segundo e terceiro
        # os números utilizados para os cálculos.

    ###
    def soma(self, n1, n2):
        data = f'1;{n1};{n2}'
        return criaConexao(self, data)

    def produto(self, n1, n2):
        data = f'2;{n1};{n2}'
        return criaConexao(self, data)

    def fatorial(self, number):
        data = f'3;{number}'
        return criaConexao(self, data)