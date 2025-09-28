import os
import re
import telebot

# ⚠️ REMPLACEZ PAR VOTRE VRAI TOKEN
BOT_TOKEN = "8325290073:AAGfd9smVVktuirTO8CIOc2qV6MUlAGiE3o"
bot = telebot.TeleBot(BOT_TOKEN)

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
            return "❌ Dossier 'fiches' introuvable"
        
        print("✅ Dossier 'fiches' trouvé")
        
        # Chemin du fichier
        chemin_fichier = os.path.join("fiches", "test.txt")
        print(f"📁 Chemin fichier: {chemin_fichier}")
        
        if not os.path.exists(chemin_fichier):
            print("❌ Fichier test.txt INTROUVABLE")
            return "❌ Fichier test.txt introuvable"
        
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
                        print(f"📤 Envoi fiche de {len(fiche_propre)} caractères")
                        return f"✅ FICHE TROUVÉE :\n\n{fiche_propre}"
            
            return "❌ Fiche trouvée mais erreur d'extraction"
        else:
            print(f"❌ NUMÉRO NON TROUVÉ dans le fichier")
            return f"❌ Aucune fiche trouvée pour {numero}"
            
    except Exception as e:
        print(f"💥 ERREUR: {e}")
        return f"❌ Erreur: {e}"

@bot.message_handler(commands=['start'])
def start(message):
    print(f"\n🎯 /start reçu de: {message.from_user.username}")
    bot.reply_to(message, "🤖 Bot actif! Testez /number 0667324073")

@bot.message_handler(commands=['number'])
def number(message):
    print(f"\n📱 /number reçu: '{message.text}'")
    print(f"👤 De: {message.from_user.username}")
    
    parts = message.text.split()
    print(f"🔍 Parts: {parts}")
    
    if len(parts) < 2:
        print("❌ Pas de numéro fourni")
        bot.reply_to(message, "❌ Usage: /number 0678907644")
        return
    
    numero = parts[1]
    print(f"🔍 Numéro extrait: '{numero}'")
    
    resultat = rechercher_fiche_par_numero(numero)
    print(f"📤 Résultat à envoyer: {len(resultat)} caractères")
    
    bot.reply_to(message, resultat)
    print("✅ Message envoyé!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(f"📨 Message: '{message.text}'")
    bot.reply_to(message, "❌ Commande inconnue. Utilisez /help")

print("\n🚀 Bot en attente de messages...")
print("💡 Testez avec: /number 0667324073")
print("💡 Testez avec: /number 0631057528")
bot.polling()