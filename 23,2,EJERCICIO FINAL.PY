import openai

openai.api_key = ""

from openai import OpenAI

client = OpenAI(api_key=openai.api_key)

system_rol = '''
Hace de cuenta que sos un analizador de sentimientos.
Yo te paso sentimientos y vos analizas el sentimiento de los mensajes
y me das una respuesta con al menos 1 caracter y como máximo 4 caracteres
SOLO RESPUESTAS NUMÉRICAS. donde -1 es negatividad máxima, 0 es neutral y 1 es positividad máxima.
(Podés responder solo con ints o floats)
'''

mensajes = [{"role": "system", "content": system_rol}]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.6 and polaridad <= 0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m"
        elif polaridad > -0.3 and polaridad < 0.1:
            return "\x1b[1;31m" + "Algo negativo" + "\x1b[0;37m"
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo" + "\x1b[0;37m"
        elif polaridad >= 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy positivo" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "MUY Negativo" + "\x1b[0;37m"

analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\nDecime Algo: " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=mensajes,
        max_tokens=8
    )

    respuesta = completion.choices[0].message.content
    mensajes.append({"role": "assistant", "content": respuesta})

    try:
        polaridad = float(respuesta)
    except:
        polaridad = 0

    sentimiento = analizador.analizar_sentimiento(polaridad)
    print(sentimiento)
