import sqlite3
import asyncio
from os import getenv
from tgbot_lib import enviar_mensagem

def conectar_db():
    conector = sqlite3.connect('./db/estoque.db')
    return conector

def criar_tabela():
    
    # Comando SQL para criar a tabela de produtos
    conector = conectar_db()
    cursor = conector.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comandos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id TEXT NOT NULL,
        nome_comando VARCHAR(50) NOT NULL,
        mensagem TEXT
    )
    """)

    conector.commit()
    conector.close()


async def adicionar_produto(nome, quantidade, valor):
    conector = conectar_db()
    cursor = conector.cursor()
    
    cursor.execute("""
    INSERT INTO produtos (nome, quantidade, preco)
    VALUES (?, ?, ?)
    """, (nome, quantidade, valor))
    
    conector.commit()
    conector.close()

async def atualizar_quantidade_produto(produto_id, quantidade):
    conector = conectar_db()
    cursor = conector.cursor()
    cursor.execute("""
    UPDATE produtos
    SET quantidade = ?
    WHERE id = ?
    """, (quantidade, produto_id))
    conector.commit()
    conector.close()

async def procurar_estoque(produto: str, chat_id):
    conector = conectar_db()
    cursor = conector.cursor()
    cursor.execute("""
    SELECT * FROM produtos
    WHERE Nome = ?
    """, (produto.title(),))
    info_produto = cursor.fetchone()
    conector.close()


    if info_produto:
        text = f"""---------------------------\n*PRODUTO*\n---------------------------
Id: {info_produto[0]}
Nome: {info_produto[1]}
Quantidade: {info_produto[2]}
Valor: {info_produto[3]}s
"""
    else:
        text = f"Produto '{produto}' não encontrado."
    print(text)
    await enviar_mensagem(chat_id=chat_id, text=text)

    await apagar_comando(chat_id)

    return produto

async def ver_estoque(chat_id):
    conector = conectar_db()
    cursor = conector.cursor()
    cursor.execute("""
    SELECT * FROM produtos
    """)
    produtos = cursor.fetchall()
    conector.close()

    text = '---------------------------\n*ESTOQUE*\n--------------------------- \n'

    for produto in produtos:
        text_prod = f"""Id: {produto[0]}
Nome: {produto[1]}
Quantidade: {produto[2]}
Valor: {produto[3]}
---------------------------
"""
        text+=text_prod
    
    print(text)
    await enviar_mensagem(chat_id=chat_id, text=text)

    return produtos

async def deletar_produto(id):
    conector = conectar_db()
    cursor = conector.cursor()
    cursor.execute("""
    DELETE FROM produtos
    WHERE id = ?
    """, (id,))
    conector.commit()
    conector.close()

async def verificar_estoque(id, chat_id = None):
    conector = conectar_db()
    cursor = conector.cursor()
    cursor.execute("""
    SELECT nome, quantidade FROM produtos
    WHERE id = ?
    """, (id,))
    produto = cursor.fetchone()
    conector.close()

    if chat_id:
        if produto[1] <= 5:
            titulo_text = "Alerta - Estoque baixo!\n"

            if produto[1] <= 3:
                titulo_text = "Crítico - Estoque quase no fim!\n"

            text = f"""
Produto: {produto[0]}
Quantidade: {produto[1]}
        """

            text = titulo_text+text

            await enviar_mensagem(text, chat_id)

    return produto


# funções de comandos

async def add_comando(chat_id, comando):
    conector = conectar_db()
    cursor = conector.cursor()
    
    cursor.execute("""
    INSERT INTO comandos (chat_id, nome_comando)
    VALUES (?, ?)
    """, (chat_id, comando))
    
    conector.commit()
    conector.close()

async def add_comando_msg(chat_id, mensagem):
    conector = conectar_db()
    cursor = conector.cursor()
    cursor.execute("""
    UPDATE comandos
    SET mensagem = ?
    WHERE chat_id = ?
    """, (mensagem, chat_id))
    conector.commit()
    conector.close()

async def verificar_comando(chat_id):
    conector = conectar_db()
    cursor = conector.cursor()
    cursor.execute("""
    SELECT * FROM comandos
    WHERE chat_id = ?
    """, (chat_id,))
    resultado = cursor.fetchone()
    conector.close()
    if resultado:
        return True
    return False

async def apagar_comando(chat_id):
    conector = conectar_db()
    cursor = conector.cursor()
    cursor.execute("""
    DELETE FROM comandos
    WHERE chat_id = ?
    """, (chat_id,))
    conector.commit()
    conector.close()

if __name__ == "__main__":
    chat_id = getenv('chat_id')
    # asyncio.run(add_comando_msg(chat_id, 'test'))
    # asyncio.run(apagar_comando('chat_id'))
    # asyncio.run(deletar_produto('1'))
    asyncio.run(atualizar_quantidade_produto('3', 10))
    asyncio.run(atualizar_quantidade_produto('4', 10))
    asyncio.run(atualizar_quantidade_produto('5', 10))
    # criar_tabela()



