import paho.mqtt.client as mqtt
import time
from hal import temperatura, rele
from definicoes import usuario2, senha2, cliente_id2, servidor2, porta2

def main():
    
    # Método para resposta das mensagens
    def mensagem(client, user, msg):
        vetor = msg.payload.decode().split(',')
        print('Temperatura atual da ESTUFA 2 é {:.1f} °C.'.format(temp))
        rele('ligado' if vetor[1] == '1' and temp < 30 else 'desligado')
        cliente.publish(f'v1/{usuario2}/things/{cliente_id2}/response', f'ok,{vetor[0]}')

    # Conexão inicial
    cliente = mqtt.Client(cliente_id2)
    cliente.username_pw_set(usuario2, senha2)
    cliente.connect(servidor2, porta2)

    # Subscribe
    cliente.on_message = mensagem
    cliente.subscribe(f'v1/{usuario2}/things/{cliente_id2}/cmd/2')
    cliente.loop_start()

    # Publish
    while True:
        temp = temperatura()
        cliente.publish(f'v1/{usuario2}/things/{cliente_id2}/data/3', 'temp,c=' + str(temp))
        time.sleep(10)

    #cliente.disconnect()

if __name__ == "main":
    main()