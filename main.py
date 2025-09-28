import os
import re
import time
import telebot
from telebot import apihelper
from design import BotDesign

# ⚠️ REMPLACEZ PAR VOTRE VRAI TOKEN
BOT_TOKEN = "8325290073:AAGfd9smVVktuirTO8CIOc2qV6MUlAGiE3o"
bot = telebot.TeleBot(BOT_TOKEN)

# Configuration pour éviter les conflits
apihelper.RETRY_ON_ERROR = True
apihelper.MAX_RETRIES = 3
apihelper.TIMEOUT = 30

print("=== BOT DÉMARRÉ ===")
print("✅ Bot créé avec succès")

def rechercher_fiche_par_numero(numero):
    """Recherche une fiche par numéro de téléphone"""
    try:
        print(f"\n=== DÉBUT RECHERCHE ===")
        print(f"🔍 Numéro à rechercher: '{numero}'")
        
        # Nettoyer le numéro
        numero_clean = re.sub(r'\D', '', numero)
        print(f"🔍 Numéro nettoyé: '{numero_clean}'")
        
        # Vérifier le dossier fiches
        if not os.path.exists("fiches"):
            print("❌ Dossier 'fiches' INTROUVABLE")
            return BotDesign.error_system("Dossier 'fiches' introuvable")
        
        print("✅ Dossier 'fiches' trouvé")
        
        # Chemin du fichier
        chemin_fichier = os.path.join("fiches", "test.txt")
        print(f"📁 Chemin fichier: {chemin_fichier}")
        
        if not os.path.exists(chemin_fichier):
            print("❌ Fichier test.txt INTROUVABLE")
            return BotDesign.error_system("Fichier test.txt introuvable")
        
        print("✅ Fichier test.txt trouvé")
        
        # Lire le fichier
        print("📖 Lecture du fichier...")
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            contenu_complet = f.read()
        
        print(f"📊 Taille fichier: {len(contenu_complet)} caractères")
        
        # Vérifier si le numéro est dans le fichier
        if numero_clean in contenu_complet:
            print(f"🎯 NUMÉRO TROUVÉ dans le fichier!")
            
            # Séparer les fiches
            fiches = contenu_complet.split('---------------------------------')
            print(f"📋 Nombre de fiches séparées: {len(fiches)}")
            
            # Trouver la bonne fiche
            for i, fiche in enumerate(fiches):
                if numero_clean in fiche:
                    print(f"✅ Fiche exacte trouvée: #{i+1}")
                    fiche_propre = fiche.strip()
                    if fiche_propre:
                        print(f"📤 Envoi fiche formatée")
                        return BotDesign.format_fiche(fiche_propre, numero_clean)
            
            return BotDesign.error_system("Fiche trouvée mais erreur d'extraction")
        else:
            print(f"❌ NUMÉRO NON TROUVÉ dans le fichier")
            return BotDesign.error_not_found(numero)
            
    except Exception as e:
        print(f"💥 ERREUR: {e}")
        return BotDesign.error_system(str(e))

@bot.message_handler(commands=['start'])
def start(message):
    print(f"\n🎯 /start reçu de: {message.from_user.username}")
    bot.reply_to(message, BotDesign.welcome_message(), parse_mode='HTML')

@bot.message_handler(commands=['number'])
def number(message):
    print(f"\n📱 /number reçu: '{message.text}'")
    print(f"👤 De: {message.from_user.username}")
    
    parts = message.text.split()
    print(f"🔍 Parts: {parts}")
    
    if len(parts) < 2:
        print("❌ Pas de numéro fourni")
        bot.reply_to(message, BotDesign.error_syntax(), parse_mode='HTML')
        return
    
    numero = parts[1]
    print(f"🔍 Numéro extrait: '{numero}'")
    
    # Message de recherche en cours
    msg = bot.reply_to(message, BotDesign.searching_message(numero), parse_mode='HTML')
    
    # Faire la recherche
    resultat = rechercher_fiche_par_numero(numero)
    print(f"📤 Résultat à envoyer: {len(resultat)} caractères")
    
    # Supprimer le message "recherche en cours" et envoyer le résultat
    try:
        bot.delete_message(message.chat.id, msg.message_id)
    except:
        pass
    
    bot.reply_to(message, resultat, parse_mode='HTML')
    print("✅ Message envoyé!")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, BotDesign.help_message(), parse_mode='HTML')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(f"📨 Message: '{message.text}'")
    bot.reply_to(message, BotDesign.unknown_command(), parse_mode='HTML')

# Fonction principale avec gestion des erreurs
def main():
    print("\n🚀 Bot Noleak Database Premium démarré!")
    print("💡 Testez avec: /number 0667324073")
    print("💡 Testez avec: /number 0631057528")
    
    max_retries = 5
    retry_delay = 10  # secondes
    
    for attempt in range(max_retries):
        try:
            print(f"🚀 Tentative de démarrage {attempt + 1}/{max_retries}...")
            bot.infinity_polling(timeout=30, long_polling_timeout=30)
            break
            
        except Exception as e:
            print(f"❌ Erreur lors du démarrage: {e}")
            
            if attempt < max_retries - 1:
                print(f"⏳ Nouvelle tentative dans {retry_delay} secondes...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Backoff exponentiel
            else:
                print("💥 Échec après plusieurs tentatives")
                raise

if __name__ == "__main__":
    main()
