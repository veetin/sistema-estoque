from loguru import logger
from menu_estoque import menu_editar_estoque, menu_estoque
from database import procurar_estoque, ver_estoque, add_comando
from tgbot_lib import confirmar_callback, enviar_mensagem


async def processar_callback(data: dict, chat_id):
    try:
        # armazenando qual o botão apertado
        
        callback_data = data['callback_query']

        botao = callback_data['data']
        callback_id = callback_data['id']

        if await confirmar_callback(callback_id=callback_id):

            if botao == 'menu_editar_estoque':
                message_id = callback_data['message']['message_id']
                await menu_editar_estoque(chat_id, message_id)
            
            elif botao == 'voltar_menu_estoque':
                message_id = callback_data['message']['message_id']
                await menu_estoque(chat_id, callback=True, message_id=message_id)
            
            elif botao == 'menu_ver_estoque':
                produtos = await ver_estoque(chat_id)
                print(produtos[1][1])
            
            elif botao == 'menu_procurar_estoque':
                await add_comando(chat_id, botao)
                text = 'Informe no nome do produto:'
                await enviar_mensagem(chat_id=chat_id, text=text)
                
    
    except Exception as e:
        logger.error({
                'status:': 'falha ao processar callback',
                'erro': str(e)
                })