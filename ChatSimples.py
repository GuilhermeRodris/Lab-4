import socket  
  
IP_destino = "192.168.0.12"  
PORTA_destino = 32012          
MENSAGEM = "Chat aberto"
 
print ("Endereço IP de destino:", IP_destino)
print ("Porta UDP de destino:", PORTA_destino)
print ("Mensagem enviada:", MENSAGEM)
 

while (MENSAGEM != "QUIT"):
    MENSAGEM = input("Digite a mensagem: ")
    if (MENSAGEM == "QUIT"):
        MENSAGEM = "Fim da transmicao"
        print("Fim da transmicao")
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(MENSAGEM.encode('UTF-8'), (IP_destino, PORTA_destino))
    if (MENSAGEM == "Fim da transmicao"):
        MENSAGEM = "QUIT"

    
