from http import HTTPStatus
from fastapi import FastAPI, HTTPException, Request
import uvicorn
from loguru import logger
from menu_estoque import menu_estoque
from verificar_comando import verificar_comando
from menu_estoque import menu_editar_estoque
from tgbot_lib import confirmar_callback

app = FastAPI()

logger.add('estoque.log')

@app.post('/webhook')
async def webhook(request: Request):
    try:
        data = await request.json()
        logger.info(data)

        comando = await verificar_comando(data)
        
        if comando:
            
            chat_id = str(data['message']['chat']['id'])
            
            # comando para exibir o menu
            if  comando == '/menu':
                await menu_estoque(chat_id)
                
        elif 'callback_query' in data:
            logger.info('callback')

            callback_data = data['callback_query']

            # armazenando o id do chat
            chat_id = str(callback_data['message']['chat']['id'])

            comando = callback_data['data']

            callback_id = callback_data['id']

            if await confirmar_callback(callback_id=callback_id):

                if comando == 'menu_editar_estoque':
                    message_id = callback_data['message']['message_id']
                    await menu_editar_estoque(chat_id, message_id)
                
                elif comando == 'voltar_menu_estoque':
                    message_id = callback_data['message']['message_id']
                    await menu_estoque(chat_id, callback=True, message_id=message_id)
                    
            
    
    except Exception as e:
        logger.error({
                'status:': 'falha ao processar os dados',
                'erro': str(e)
                })
        
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail={
                'status:': 'falha ao processar os dados',
                'erro': f'{e}'
                }
        )




