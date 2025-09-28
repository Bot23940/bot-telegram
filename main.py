import os
import re
import telebot
import time

# Token du bot
BOT_TOKEN = "8325290073:AAGfd9smVVktuirTO8CIOc2qV6MUlAGiE3o"
bot = telebot.TeleBot(BOT_TOKEN)

print("🔄 Démarrage du bot...")
print("📡 Vérification des instances en conflit...")

def rechercher_fiche_par_numero(numero):
    """Recherche une fiche par numéro de téléphone"""
    try:
        numero_clean = re.sub(r'\D', '', numero)
        
        if not os.path.exists("fiches/test.txt"):
            return "❌ Fichier introuvable"
        
        with open("fiches/test.txt", 'r', encoding='utf-8') as f:
            contenu_complet = f.read()
        
        if numero_clean in contenu_complet:
            fiches = contenu_complet.split('---------------------------------')
            for fiche in fiches:
                if numero_clean in fiche:
                    return f"✅ FICHE TROUVÉE :\n\n{fiche.strip()}"
        
        return f"❌ Aucune fiche trouvée pour {numero}"
            
    except Exception as e:
        return f"❌ Erreur: {e}"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Bot ACTIF ! Utilise /number 0667324073")

@bot.message_handler(commands=['number'])
def number(message):
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "❌ Usage: /number 0678907644")
        return
    
    numero = parts[1]
    resultat = rechercher_fiche_par_numero(numero)
    bot.reply_to(message, resultat)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "❌ Commande inconnue. Utilisez /help")

# DÉMARRAGE SÉCURISÉ
if __name__ == "__main__":
    print("🚀 Lancement en mode sécurisé...")
    
    try:
        # Essayer de démarrer avec timeout
        bot.polling(none_stop=True, timeout=60)
    except telebot.apihelper.ApiTelegramException as e:
        if "409" in str(e):
            print("💥 CONFLIT DÉTECTÉ : Une autre instance tourne encore")
            print("🛑 Arrêt de cette instance pour éviter les doublons")
        else:
            print(f"💥 Autre erreur: {e}")
    except Exception as e:
        print(f"💥 Erreur générale: {e}")
