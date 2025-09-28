import os
import re
import telebot
from datetime import datetime

BOT_TOKEN = "8325290073:AAGfd9smVVktuirTO8CIOc2qV6MUlAGiE3o"
bot = telebot.TeleBot(BOT_TOKEN)

# FONCTIONS DE DESIGN DIRECTES DANS LE FICHIER
def design_welcome():
    return """🎨 <b>🤖 BIENVENUE SUR NOLEAK DATABASE</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>🚀 COMMANDES DISPONIBLES</b>
├─ <code>/number XXXXXXXXXX</code> - Recherche
├─ <code>/help</code> - Centre d'aide

<b>💡 EXEMPLE</b>
<code>/number 0667324073</code>

🔒 <b>SYSTÈME SÉCURISÉ</b>"""

def design_format_fiche(fiche_brute, numero):
    """Formate une fiche en version jolie"""
    try:
        lignes = fiche_brute.split('\n')
        
        # Extraire le nom
        nom = ""
        for ligne in lignes:
            ligne_clean = ligne.strip()
            if ligne_clean and not ligne_clean.startswith('Né(e)') and not ligne_clean.startswith('Adresse'):
                nom = ligne_clean
                break
        
        # Extraire les informations
        infos = {}
        for ligne in lignes:
            if ':' in ligne:
                key, value = ligne.split(':', 1)
                infos[key.strip()] = value.strip()
        
        heure = datetime.now().strftime("%H:%M")
        date = datetime.now().strftime("%d/%m/%Y")
        
        return f"""🎨 <b>🔍 RECHERCHE TELEPHONIQUE</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📊 IDENTIFICATION</b>
├─ <b>👤 Nom:</b> {nom}
├─ <b>🎂 Naissance:</b> {infos.get('Né(e) le', 'Non renseigné')}

<b>📍 LOCALISATION</b>
├─ <b>🏠 Adresse:</b> {infos.get('Adresse', 'Non renseigné')}
└─ <b>🌆 Ville:</b> {infos.get('Ville', 'Non renseigné')}

<b>📞 COORDONNÉES</b>
├─ <b>📱 Téléphone:</b> <code>{infos.get('Téléphone(s)', 'Non renseigné')}</code>
└─ <b>📧 Email:</b> <code>{infos.get('Email', 'Non renseigné')}</code>

━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ <b>RÉUSSITE</b> • 📅 {date} • 🕒 {heure}"""
    
    except Exception as e:
        return f"❌ Erreur formatage: {e}"

# FONCTION DE RECHERCHE
def rechercher_fiche(numero):
    try:
        numero_clean = re.sub(r'\D', '', numero)
        
        if not os.path.exists("fiches/test.txt"):
            return "❌ Fichier introuvable"
        
        with open("fiches/test.txt", 'r', encoding='utf-8') as f:
            content = f.read()
        
        fiches = content.split('---------------------------------')
        
        for fiche in fiches:
            if numero_clean in fiche:
                return design_format_fiche(fiche.strip(), numero_clean)
        
        return f"❌ Aucune fiche pour {numero}"
        
    except Exception as e:
        return f"❌ Erreur: {e}"

# HANDLERS DU BOT
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, design_welcome(), parse_mode='HTML')

@bot.message_handler(commands=['number'])
def number_cmd(message):
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "❌ Usage: /number 0612345678")
        return
    
    numero = parts[1]
    resultat = rechercher_fiche(numero)
    bot.reply_to(message, resultat, parse_mode='HTML')

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, design_welcome(), parse_mode='HTML')

print("🚀 Bot démarré!")
bot.polling()
