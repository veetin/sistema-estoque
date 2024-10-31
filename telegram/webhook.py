from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/webhook')
async def webhook(request: Request):
    mensagem = await request.json()
    print(mensagem)