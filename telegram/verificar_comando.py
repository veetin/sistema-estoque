async def verificar_comando(data):
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
        return False