import httpx
from loguru import logger
from os import getenv

BOT_TOKEN = getenv('bot_token')
TELEGRAM_API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'

def definir_webhook(url:str) -> dict:
    endpoint = TELEGRAM_API_URL+"/setWebhook"
    
    payload = {
        "url":url
    }

    response = httpx.post(url=endpoint, json=payload)

    return response.json()

def deletar_webhook() -> dict:
    endpoint = TELEGRAM_API_URL+"/deleteWebhook"
    response = httpx.get(url=endpoint)

    return response.json()

async def enviar_mensagem(text: str, chat_id: str, parse_mode: str = "Markdown", inline_keyboard = None) -> dict:
    try:
        endpoint = TELEGRAM_API_URL+"/sendMessage"

        payload = {
            'text': text,
            'chat_id': chat_id,
            'parse_mode': parse_mode
        }


        if inline_keyboard:
            payload['reply_markup'] =inline_keyboard

        response = httpx.post(url=endpoint, json=payload)
        response.raise_for_status()

        if response.json()['ok']:
            return response.json()
        else:
            logger.error({
            'status:': 'Falha ao enviar mensagem',
            'erro': response.json()
            })
            raise "Falha ao enviar mensagem"
    
    except Exception as e:
        logger.error({
        'status:': 'falha ao enviar a mensagem para o telegram',
        'erro': f'{e}'
        })

async def atualizar_mensagem(text: str, chat_id: str, mensagem_id: str, parse_mode: str = "Markdown", inline_keyboard = None) -> dict:
    try:
        endpoint = TELEGRAM_API_URL+"/editMessageText"

        payload = {
            'text': text,
            'message_id': mensagem_id,
            'chat_id': chat_id,
            'parse_mode': parse_mode
        }


        if inline_keyboard:
            payload['reply_markup'] =inline_keyboard

        response = httpx.post(url=endpoint, json=payload)
        response.raise_for_status()

        if response.json()['ok']:
            return response.json()
        else:
            logger.error({
            'status:': 'Falha ao enviar mensagem',
            'erro': response.json()
            })
            raise "Falha ao enviar mensagem"
    
    except Exception as e:
        logger.error({
        'status:': 'falha ao enviar a mensagem para o telegram',
        'erro': f'{e}'
        })

async def confirmar_callback(callback_id: str):
    try:
        print(BOT_TOKEN)
        endpoint = f'{TELEGRAM_API_URL}/answerCallbackQuery'
        response = httpx.post(url=endpoint, data={
        'callback_query_id': callback_id
        })
        response.raise_for_status()
        
        if response.json()['ok']:
            return response.json()['ok']
        else:
            return False

    except Exception as e:
        logger.error({
        'status:': 'falha ao enviar confirmação de resposta para o telegram.',
        'erro': f'{e}'
    })