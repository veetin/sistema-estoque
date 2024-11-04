from database import verificar_estoque, atualizar_quantidade_produto
import asyncio
from os import getenv
from dotenv import load_dotenv

async def realizar_venda():
    load_dotenv('.env')
    chat_id = getenv('chat_id')
    text = """
---------------------
| SISTEMA DE VENDAS |
---------------------

Produtos:
[ 3 ] - Telefone
[ 4 ] - Televisão
[ 5 ] - Notebook
"""
    print(text)
    
    opcao = input("Informe o produto: ")
    quantidade = int(input('Informe a quantidade: '))

    estoque = await verificar_estoque(opcao)
    
    if  estoque[1] >= quantidade:
        print(f'Venda Realiza!')
        print(f'Produto: {estoque[0]}\nQuantidade comprada: {quantidade}')

        
        atualizar_estoque = estoque[1] - quantidade

        await atualizar_quantidade_produto(opcao, atualizar_estoque)
        await verificar_estoque(opcao, chat_id)

    else:
        print(f'Estoque insuficiênte')
        print(f'Quantidade no estoque: {estoque[1]}')

if __name__ == "__main__":
    asyncio.run(realizar_venda())