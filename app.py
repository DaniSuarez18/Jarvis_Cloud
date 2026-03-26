import telebot
from groq import Groq

# --- CONFIGURACIÓN ---
TELEGRAM_TOKEN = "8668304325:AAE6xV1TV8y2xlOOcnQFsh1I3FSKyXJkbpc"
GROQ_API_KEY = "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"

# Inicializar clientes
client = Groq(api_key=GROQ_API_KEY)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def responder(message):
    try:
        # Usamos el modelo Llama 3 (es igual de potente que Gemini)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Eres Jarvis, el asistente personal de ingeniería de Santiago. Eres culto y eficiente."
                },
                {
                    "role": "user",
                    "content": message.text,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        
        respuesta = chat_completion.choices[0].message.content
        bot.reply_to(message, respuesta)
    except Exception as e:
        bot.reply_to(message, f"Señor, hubo un error técnico: {e}")

if __name__ == "__main__":
    print("Jarvis (vía Groq) está ONLINE...")
    bot.infinity_polling()
