from loguru import logger
from tgbot_lib import enviar_mensagem
import httpx
from os import getenv

BOT_TOKEN = getenv('bot_token')

async def menu_estoque(chat_id):
    try:
        # Texto que será enviado na mensagem do bot
        text = """
-----------------------------------
| *MENU DO ESTOQUE* |
-----------------------------------
"""
        
        # Define os botões de opções que o usuário verá no menu
        inline_keyboard = {
                'inline_keyboard': [
                    [
                        {
                            'text': 'Procurar Produto',  # Texto do botão "Ordem Aberta"
                            'callback_data':'menu_procurar_produto',  # Dado enviado quando o botão é clicado
                        },
                        
                        {
                            'text': 'Editar Estoque',  # Texto do botão "Ordem Aberta"
                            'callback_data':'menu_editar_estoque',  # Dado enviado quando o botão é clicado
                        }
                        
                    ],
                    [
                        {
                            'text': 'Ver Estoque',  # Texto do botão "Sem Ordem"
                            'callback_data':'menu_ver_estoque',  # Dado enviado quando o botão é clicado
                        }
                        
                    ]
                    
                ]
            }

        # Envia a mensagem com os botões para o usuário no Telegram e armazena a resposta
        response = await enviar_mensagem(text=text, chat_id=chat_id, inline_keyboard=inline_keyboard)
        logger.info(f'Menu de estoque enviado com sucesso.\nresponse: {response}')

    except Exception as e:
        logger.error(f"Falha ao enviar menu do estoque\nerror: {e}")


async def menu_editar_estoque(chat_id, message_id):
    try:
        # Define o novo teclado inline para a opção "Atualizar Estoque"
        inline_keyboard = {
            'inline_keyboard': [
                [
                    {
                        'text': 'Adicionar Produto',  # Texto do botão "Ordem Aberta"
                        'callback_data':'menu_adicionar_produto',  # Dado enviado quando o botão é clicado
                    },
                    {
                        'text': 'Atualizar Produto',  # Texto do botão "Sem Ordem"
                        'callback_data':'menu_atualizar_estoque',  # Dado enviado quando o botão é clicado
                    }
                ],
                [   
                    {
                        'text': 'Apagar Produto',  # Texto do botão "Sem Ordem"
                        'callback_data':'menu_apagar_produto',  # Dado enviado quando o botão é clicado
                    },
                    
                    {
                        'text': 'Voltar',
                        'callback_data': 'voltar_menu_estoque'
                    }
                ]
            ]
        }

        # Configura o payload para editar a mensagem
        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'text': 'Selecione a ação para atualizar o estoque:',
            'reply_markup': inline_keyboard
        }

        print('teste')
        # Faz a requisição para editar a mensagem com o novo teclado
        async with httpx.AsyncClient() as client:
            await client.post(f'https://api.telegram.org/bot{BOT_TOKEN}/editMessageText', json=payload)

    except Exception as e:
        logger.error(f"Erro ao atualizar o menu do estoque\nerror: {e}")


