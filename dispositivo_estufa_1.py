import paho.mqtt.client as mqtt
import time
from hal import temperatura, rele
from definicoes import usuario1, senha1, cliente_id1, servidor1, porta1

def main():
    
    # Método para resposta das mensagens
    def mensagem(client, user, msg):
        vetor = msg.payload.decode().split(',')
        print('Temperatura atual da ESTUFA 1 é {:.1f} °C.'.format(temp))
        rele('ligado' if vetor[1] == '1' and temp < 30 else 'desligado')
        cliente.publish(f'v1/{usuario1}/things/{cliente_id1}/response', f'ok,{vetor[0]}')

    # Conexão inicial
    cliente = mqtt.Client(cliente_id1)
    cliente.username_pw_set(usuario1, senha1)
    cliente.connect(servidor1, porta1)

    # Subscribe
    cliente.on_message = mensagem
    cliente.subscribe(f'v1/{usuario1}/things/{cliente_id1}/cmd/0')
    cliente.loop_start()

    # Publish
    while True:
        temp = temperatura()
        cliente.publish(f'v1/{usuario1}/things/{cliente_id1}/data/1', 'temp,c=' + str(temp))
        time.sleep(10)

    #cliente.disconnect()

if __name__ == "main":
    main()