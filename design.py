from datetime import datetime

class BotDesign:
    """Classe pour le design beau du bot"""
    
    @staticmethod
    def welcome_message():
        return """🎨 <b>🤖 BIENVENUE SUR NOLEAK DATABASE</b>
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

🔒 <b>SYSTÈME SÉCURISÉ • RECHERCHE INSTANTANÉE</b>"""
    
    @staticmethod
    def help_message():
        return """🎨 <b>📋 CENTRE D'AIDE NOLEAK</b>
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

📞 <b>SUPPORT:</b> Contactez l'administrateur"""
    
    @staticmethod
    def error_syntax():
        return """🎨 <b>❌ ERREUR DE SYNTAXE</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💡 UTILISATION CORRECTE</b>
<code>/number 0612345678</code>

<b>📋 EXEMPLES CONCRETS</b>
├─ <code>/number 0631057528</code>
├─ <code>/number 0667324073</code>
└─ <code>/number 0675448532</code>

🔧 <b>Format: 10 chiffres requis</b>"""
    
    @staticmethod
    def searching_message(numero):
        return f"""🎨 <b>🔍 LANCEMENT DE LA RECHERCHE</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📞 NUMÉRO CIBLÉ:</b> <code>{numero}</code>
<b>⏳ STATUT:</b> Analyse en cours...

<b>🔄 PROCESSUS:</b>
├─ Vérification base de données
├─ Extraction des informations  
├─ Formatage des résultats
└─ Préparation de l'affichage

<i>⏰ Veuillez patienter quelques secondes</i>"""
    
    @staticmethod
    def format_fiche(fiche_brute, numero):
        """Formate une fiche en version ultra jolie"""
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
        
        # Formater le résultat
        heure_actuelle = datetime.now().strftime("%H:%M")
        date_actuelle = datetime.now().strftime("%d/%m/%Y")
        
        return f"""🎨 <b>🔍 RECHERCHE TELEPHONIQUE</b>
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
✅ <b>RECHERCHE RÉUSSIE</b> • 📅 {date_actuelle} • 🕒 {heure_actuelle}"""
    
    @staticmethod
    def error_not_found(numero):
        return f"""🎨 <b>🔍 RECHERCHE INFructueuse</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

📞 <b>Numéro recherché:</b> <code>{numero}</code>
❌ <b>Statut:</b> Aucun résultat

💡 <b>Suggestions:</b>
• Vérifiez le numéro
• Format: 10 chiffres
• Essayez un autre numéro

🕒 {datetime.now().strftime("%H:%M")} • 🔍 Recherche terminée"""
    
    @staticmethod
    def error_system(e):
        return f"""🎨 <b>❌ ERREUR SYSTÈME</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ <b>Erreur technique:</b> {e}
🔧 <b>Solution:</b> Contactez l'administrateur

🛠️ Système de recherche temporairement indisponible"""
    
    @staticmethod
    def unknown_command():
        return """🎨 <b>❌ COMMANDE INCONNUE</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>💡 COMMANDES DISPONIBLES</b>
├─ <code>/start</code> - Menu principal
├─ <code>/number XXXXXXXXXX</code> - Recherche
├─ <code>/help</code> - Centre d'aide
└─ <code>/info</code> - Informations

<b>🔍 EXEMPLE DE RECHERCHE</b>
<code>/number 0631057528</code>

📞 <b>BESOIN D'AIDE?</b> Utilisez /help"""
