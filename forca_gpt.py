"""chat gpt para a nossa forca feliz"""
from openai import OpenAI
def palavra_gpt(dificuldade, lingua, tamanho, genero):
    client = OpenAI(api_key=("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"))

    prompt = [{"role":"user", "content":f"Me diga uma palavra da língua {lingua} com {tamanho} letras, do gênero {genero} com dificuldade {dificuldade} para um jogo da forca sem ponto final"}]

    response = client.chat.completions.create(
        messages = prompt,
        model = "gpt-3.5-turbo-0125",
        max_tokens = 1000,
        temperature = 1
    )
    return response.choices[0].message.content.lower()

