from http import HTTPStatus
from fastapi import FastAPI, HTTPException, Request
import uvicorn
from loguru import logger
from menu_estoque import menu_estoque
from verificar_comando import verificar_comando
from processar_callback import processar_callback

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
        
            chat_id = str(data['callback_query']['message']['chat']['id'])
            await processar_callback(data, chat_id)
                    
        
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




