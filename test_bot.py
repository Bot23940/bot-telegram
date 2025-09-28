import telebot
import requests

# ⚠️ REMPLACEZ PAR VOTRE VRAI TOKEN
BOT_TOKEN = "8325290073:AAGfd9smVVktuirTO8CIOc2qV6MUlAGiE3o"

print("=== TEST DE CONNEXION ===")
print(f"Token utilisé: {BOT_TOKEN}")

# Test de la connexion à l'API Telegram
try:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
    response = requests.get(url)
    print(f"Status API: {response.status_code}")
    print(f"Réponse API: {response.json()}")
except Exception as e:
    print(f"❌ Erreur API: {e}")

# Création du bot
try:
    bot = telebot.TeleBot(BOT_TOKEN)
    print("✅ Bot créé avec succès")
    
    @bot.message_handler(commands=['start'])
    def start(message):
        print("✅ Message reçu!")
        bot.reply_to(message, "🤖 Bot fonctionnel!")
    
    print("🚀 Démarrage du polling...")
    bot.polling()
    
except Exception as e:
    print(f"❌ Erreur bot: {e}")