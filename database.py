import sqlite3
import asyncio
from telegram.tgbot_lib import enviar_mensagem

def conectar_db():
    conector = sqlite3.connect('estoque.db')
    return conector

def criar_tabela():
    
    # Comando SQL para criar a tabela de produtos
    conector = conectar_db()
    cursor = conector.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER DEFAULT 0,
        preco REAL
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

async def procurar_estoque(produto, chat_id):
    conector = conectar_db()
    cursor = conector.cursor()
    cursor.execute("""
    SELECT * FROM produtos
    WHERE Nome = ?
    """, (produto,))
    produto = cursor.fetchone()
    conector.close()
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



if __name__ == "__main__":
    asyncio.run(deletar_produto(2))



