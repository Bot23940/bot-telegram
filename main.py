import os
import re
import telebot
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Token sécurisé
BOT_TOKEN = os.environ.get('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN non trouvé dans les variables d'environnement")

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
        
        # Chercher dans tous les fichiers .txt
        fichiers_trouves = []
        for filename in os.listdir("fiches"):
            if filename.endswith('.txt'):
                chemin_fichier = os.path.join("fiches", filename)
                print(f"📁 Recherche dans: {filename}")
                
                if not os.path.exists(chemin_fichier):
                    print(f"❌ Fichier {filename} INTROUVABLE")
                    continue
                
                # Lire le fichier
                with open(chemin_fichier, 'r', encoding='utf-8') as f:
                    contenu_complet = f.read()
                
                print(f"📊 Taille fichier {filename}: {len(contenu_complet)} caractères")
                
                # Vérifier si le numéro est dans le fichier
                if numero_clean in contenu_complet:
                    print(f"🎯 NUMÉRO TROUVÉ dans {filename}!")
                    
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
                                fichiers_trouves.append({
                                    'fichier': filename,
                                    'contenu': f"✅ FICHE TROUVÉE ({filename}) :\n\n{fiche_propre}"
                                })
        
        if fichiers_trouves:
            # Retourner toutes les fiches trouvées
            resultat = "\n\n".join([f['contenu'] for f in fichiers_trouves])
            return resultat
        else:
            print(f"❌ NUMÉRO NON TROUVÉ dans aucun fichier")
            return f"❌ Aucune fiche trouvée pour {numero}"
            
    except Exception as e:
        print(f"💥 ERREUR: {e}")
        return f"❌ Erreur: {e}"

@bot.message_handler(commands=['start', 'help'])
def start(message):
    print(f"\n🎯 /start reçu de: {message.from_user.username}")
    bot.reply_to(message, 
                 "🤖 **Bot de recherche de fiches**\n\n"
                 "🔍 **Commandes disponibles:**\n"
                 "/start ou /help - Affiche cette aide\n"
                 "/number <numéro> - Recherche une fiche\n\n"
                 "💡 **Exemple:** `/number 0667324073`")

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
    
    # Vérifier que c'est un numéro valide
    if not re.match(r'^[\d\s\+\.-]+$', numero):
        bot.reply_to(message, "❌ Format de numéro invalide")
        return
    
    bot.reply_to(message, "🔍 Recherche en cours...")
    
    resultat = rechercher_fiche_par_numero(numero)
    print(f"📤 Résultat à envoyer: {len(resultat)} caractères")
    
    # Envoyer le résultat (limiter la longueur pour Telegram)
    if len(resultat) > 4000:
        resultat = resultat[:4000] + "\n\n... (contenu tronqué)"
    
    bot.reply_to(message, resultat)
    print("✅ Message envoyé!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(f"📨 Message: '{message.text}'")
    bot.reply_to(message, 
                 "❌ Commande inconnue.\n\n"
                 "Utilisez /help pour voir les commandes disponibles.")

if __name__ == "__main__":
    print("\n🚀 Bot en attente de messages...")
    print("💡 Testez avec: /number 0667324073")
    print("💡 Testez avec: /number 0631057528")
    
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"💥 Erreur polling: {e}")
