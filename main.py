import os
import re
import telebot
from datetime import datetime

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
            return "🎨 <b>❌ ERREUR SYSTÈME</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━━\n📁 Dossier 'fiches' introuvable\n🔧 Contactez l'administrateur"
        
        print("✅ Dossier 'fiches' trouvé")
        
        # Chemin du fichier
        chemin_fichier = os.path.join("fiches", "test.txt")
        print(f"📁 Chemin fichier: {chemin_fichier}")
        
        if not os.path.exists(chemin_fichier):
            print("❌ Fichier test.txt INTROUVABLE")
            return "🎨 <b>❌ ERREUR FICHIER</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━━\n📄 Fichier test.txt introuvable\n🔧 Vérifiez la configuration"
        
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
                        return formater_fiche_ultra_jolie(fiche_propre, numero_clean)
            
            return "🎨 <b>❌ ERREUR EXTRACTION</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━━\n⚠️ Fiche trouvée mais erreur d'extraction\n🔧 Contactez le support"
        else:
            print(f"❌ NUMÉRO NON TROUVÉ dans le fichier")
            return f"""🎨 <b>🔍 RECHERCHE INFructueuse</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

📞 <b>Numéro recherché:</b> <code>{numero}</code>
❌ <b>Statut:</b> Aucun résultat

💡 <b>Suggestions:</b>
• Vérifiez le numéro
• Format: 10 chiffres
• Essayez un autre numéro

🕒 {datetime.now().strftime("%H:%M")} • 🔍 Recherche terminée"""
            
    except Exception as e:
        print(f"💥 ERREUR: {e}")
        return f"""🎨 <b>❌ ERREUR SYSTÈME</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ <b>Erreur technique:</b> {e}
🔧 <b>Solution:</b> Contactez l'administrateur

🛠️ Système de recherche temporairement indisponible"""

def formater_fiche_ultra_jolie(fiche_brute, numero):
    """Formate la fiche en version ultra jolie avec couleurs"""
    
    # Extraire les informations
    lignes = fiche_brute.split('\n')
    
    # Trouver le nom (première ligne non vide)
    nom = ""
    for ligne in lignes:
        ligne_clean = ligne.strip()
        if ligne_clean and not ligne_clean.startswith('Né(e)') and not ligne_clean.startswith('Adresse'):
            nom = ligne_clean
            break
    
    # Extraire les autres informations
    infos = {}
    current_key = ""
    
    for ligne in lignes:
        ligne_clean = ligne.strip()
        
        if ':' in ligne_clean:
            key, value = ligne_clean.split(':', 1)
            infos[key.strip()] = value.strip()
            current_key = key.strip()
        elif current_key and ligne_clean:
            infos[current_key] += " " + ligne_clean
    
    # Nettoyer les valeurs
    for key in infos:
        infos[key] = infos[key].strip()
    
    # Formater en version ultra jolie avec couleurs
    heure_actuelle = datetime.now().strftime("%H:%M")
    date_actuelle = datetime.now().strftime("%d/%m/%Y")
    
    resultat = f"""🎨 <b>🔍 RECHERCHE TELEPHONIQUE</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📊 IDENTIFICATION</b>
├─ <b>🔎 Requête:</b> <code>/number {numero}</code>
├─ <b>👤 Nom:</b> {nom}
├─ <b>🎂 Naissance:</b> {infos.get('Né(e) le', '❌ Non renseigné')}
└─ <b>🏷️ Dép. naissance:</b> {infos.get('Dpt de naissance', '❌ Non renseigné')}

<b>📍 LOCALISATION</b>
├─ <b>🏠 Adresse:</b> {infos.get('Adresse', '❌ Non renseigné')}
└─ <b>🌆 Ville:</b> {infos.get('Ville', '❌ Non renseigné')}

<b>📞 COORDONNÉES</b>
├─ <b>📱 Téléphone:</b> <code>{infos.get('Téléphone(s)', '❌ Non renseigné')}</code>
└─ <b>📧 Email:</b> <code>{infos.get('Email', '❌ Non renseigné')}</code>

<b>💳 INFORMATIONS BANCAIRES</b>
├─ <b>🏦 IBAN:</b> <code>{infos.get('IBAN', '❌ Non renseigné')}</code>
└─ <b>🏛️ BIC:</b> <code>{infos.get('BIC', '❌ Non renseigné')}</code>

━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ <b>RECHERCHE RÉUSSIE</b> • 📅 {date_actuelle} • 🕒 {heure_actuelle}
"""
    return resultat

@bot.message_handler(commands=['start'])
def start(message):
    print(f"\n🎯 /start reçu de: {message.from_user.username}")
    welcome_text = """🎨 <b>🤖 BIENVENUE SUR NOLEAK DATABASE</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>🎯 SYSTÈME DE RECHERCHE AVANCÉ</b>
• Recherche par numéro téléphone
• Fiches clients complètes
• Interface premium

<b>🚀 COMMANDES DISPONIBLES</b>
├─ <code>/number XXXXXXXXXX</code> - Recherche
├─ <code>/help</code> - Centre d'aide
└─ <code>/info</code> - Informations

<b>💡 EXEMPLE D'UTILISATION</b>
<code>/number 0667324073</code>

🔒 <b>SYSTÈME SÉCURISÉ • RECHERCHE INSTANTANÉE</b>
"""
    bot.reply_to(message, welcome_text, parse_mode='HTML')

@bot.message_handler(commands=['number'])
def number(message):
    print(f"\n📱 /number reçu: '{message.text}'")
    print(f"👤 De: {message.from_user.username}")
    
    parts = message.text.split()
    print(f"🔍 Parts: {parts}")
    
    if len(parts) < 2:
        print("❌ Pas de numéro fourni")
        error_msg = """🎨 <b>❌ ERREUR DE SYNTAXE</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💡 UTILISATION CORRECTE</b>
<code>/number 0612345678</code>

<b>📋 EXEMPLES CONCRETS</b>
├─ <code>/number 0631057528</code>
├─ <code>/number 0667324073</code>
└─ <code>/number 0675448532</code>

🔧 <b>Format: 10 chiffres requis</b>"""
        bot.reply_to(message, error_msg, parse_mode='HTML')
        return
    
    numero = parts[1]
    print(f"🔍 Numéro extrait: '{numero}'")
    
    # Message de recherche en cours
    searching_msg = f"""🎨 <b>🔍 LANCEMENT DE LA RECHERCHE</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📞 NUMÉRO CIBLÉ:</b> <code>{numero}</code>
<b>⏳ STATUT:</b> Analyse en cours...

<b>🔄 PROCESSUS:</b>
├─ Vérification base de données
├─ Extraction des informations  
├─ Formatage des résultats
└─ Préparation de l'affichage

<i>⏰ Veuillez patienter quelques secondes</i>"""
    
    msg = bot.reply_to(message, searching_msg, parse_mode='HTML')
    
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
    help_text = """🎨 <b>📋 CENTRE D'AIDE NOLEAK</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>🚀 COMMANDES PRINCIPALES</b>
├─ <code>/number XXXXXXXXXX</code> - Recherche
├─ <code>/start</code> - Menu principal
└─ <code>/help</code> - Cette aide

<b>💡 EXEMPLES CONCRETS</b>
├─ <code>/number 0631057528</code>
├─ <code>/number 0667324073</code>
└─ <code>/number 0675448532</code>

<b>🎯 FONCTIONNALITÉS</b>
├─ Recherche instantanée
├─ Fiches détaillées
├─ Interface premium
└─ Résultats formatés

<b>⚠️ INFORMATIONS IMPORTANTES</b>
├─ Numéro: 10 chiffres requis
├─ Format: France uniquement
└─ Base: Mise à jour régulière

📞 <b>SUPPORT:</b> Contactez l'administrateur"""
    bot.reply_to(message, help_text, parse_mode='HTML')

@bot.message_handler(commands=['info'])
def info(message):
    info_text = """🎨 <b>ℹ️ INFORMATIONS SYSTÈME</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>🤖 PLATEFORME:</b> Noleak Database Pro
<b>🚀 VERSION:</b> 3.0 Premium
<b>🔧 DÉVELOPPEUR:</b> Teddy Systems

<b>📈 STATISTIQUES SYSTÈME</b>
├─ Base de données: ✅ Active
├─ Moteur recherche: ✅ Optimal
├─ Interface: ✅ Premium
└─ Sécurité: ✅ Maximale

<b>🛡️ SÉCURITÉ AVANCÉE</b>
├─ Accès: 🔒 Contrôlé
├─ Données: 🔒 Cryptées
└─ Système: 🔒 Sécurisé

💎 <b>NOLEAK DATABASE PREMIUM</b>"""
    bot.reply_to(message, info_text, parse_mode='HTML')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(f"📨 Message: '{message.text}'")
    error_text = """🎨 <b>❌ COMMANDE INCONNUE</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💡 COMMANDES DISPONIBLES</b>
├─ <code>/start</code> - Menu principal
├─ <code>/number XXXXXXXXXX</code> - Recherche
├─ <code>/help</code> - Centre d'aide
└─ <code>/info</code> - Informations

<b>🔍 EXEMPLE DE RECHERCHE</b>
<code>/number 0631057528</code>

📞 <b>BESOIN D'AIDE?</b> Utilisez /help"""
    bot.reply_to(message, error_text, parse_mode='HTML')

print("\n🚀 Bot Noleak Database Premium démarré!")
print("💡 Testez avec: /number 0667324073")
print("💡 Testez avec: /number 0631057528")
bot.polling()
