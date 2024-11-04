from database import verificar_comando, add_comando_msg, procurar_estoque
from tgbot_lib import enviar_mensagem

async def verificar_mensagem(data):
    if 'message' in data:

        # verificando se a mensagem começa com um caracter reservado
        if 'entities' in data['message']:
            
            # pegando o tipo da mensagem
            tipo_mensagem = data['message']['entities'][0]['type']

            # verifica se o tipo é comando para o bot
            if tipo_mensagem == 'bot_command':

                # armazenando o comando digitado pelo usuario 
                comando = data['message']['text']

                return comando
        else:
            chat_id = str(data['message']['chat']['id'])
            mensagem = data['message']['text']

            if await verificar_comando(chat_id):

                await add_comando_msg(chat_id, mensagem)

                await procurar_estoque(mensagem, chat_id)
    else:
        return False