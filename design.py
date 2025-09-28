from datetime import datetime

class BotDesign:
    """Classe pour le design beau avec barre verte"""
    
    @staticmethod
    def welcome_message():
        return """🔐 <b>Noleak Database</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>Système de recherche avancée</b>

<b>Commandes disponibles:</b>
• /number [numéro] - Recherche par téléphone
• /help - Aide

<b>Exemple:</b>
<code>/number 0659515481</code>

🔒 <i>Système sécurisé</i>"""
    
    @staticmethod
    def help_message():
        return """📋 <b>Centre d'aide</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>Commandes:</b>
• /number [numéro] - Recherche
• /start - Menu principal
• /help - Cette aide

<b>Exemples de recherche:</b>
• <code>/number 0631057528</code>
• <code>/number 0667324073</code>
• <code>/number 0675448532</code>

💡 <i>Le numéro doit contenir 10 chiffres</i>"""
    
    @staticmethod
    def error_syntax():
        return """❌ <b>Erreur de syntaxe</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>Utilisation correcte:</b>
<code>/number 0659515481</code>

<b>Exemples:</b>
• <code>/number 0631057528</code>
• <code>/number 0667324073</code>
• <code>/number 0675448532</code>"""
    
    @staticmethod
    def searching_message(numero):
        return f"""🔍 <b>Recherche en cours...</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

📞 <b>Numéro:</b> {numero}
⏳ <b>Statut:</b> Analyse de la base de données...

<i>Veuillez patienter</i>"""
    
    @staticmethod
    def format_fiche(fiche_brute, numero):
        """Formate une fiche avec barre verte et match found"""
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
            
            # Formater avec barre verte et match found
            heure_actuelle = datetime.now().strftime("%H:%M")
            
            return f"""
🏷️ <b>Noleak</b>
👤 <b>teddy</b>  
📞 <code>/number {numero}</code>  

🟢 <b>Match found:</b>  

<b>{nom}</b>  
🗓️ <b>Né(e) le</b> {infos.get('Né(e) le', 'Non renseigné')}  
🏠 <b>Adresse :</b> {infos.get('Adresse', 'Non renseigné')}  
📱 <b>Téléphone(s) :</b> {infos.get('Téléphone(s)', 'Non renseigné')}  
💳 <b>IBAN :</b> {infos.get('IBAN', 'Non renseigné')}  
🏦 <b>BIC :</b> {infos.get('BIC', 'Non renseigné')}  
📧 <b>Email :</b> {infos.get('Email', 'Non renseigné')}  
🌆 <b>Ville :</b> {infos.get('Ville', 'Non renseigné')}  

🕒 {heure_actuelle}
"""
        except Exception as e:
            return f"❌ Erreur formatage: {e}"
    
    @staticmethod
    def error_not_found(numero):
        return f"""❌ <b>Aucun résultat</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

📞 <b>Numéro recherché:</b> {numero}
🔍 <b>Statut:</b> Aucune correspondance

💡 <b>Suggestions:</b>
• Vérifiez le numéro
• Essayez un autre numéro"""
    
    @staticmethod
    def unknown_command():
        return """⚠️ <b>Commande non reconnue</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>Commandes disponibles:</b>
• /start - Démarrer
• /number [numéro] - Recherche
• /help - Aide

<b>Exemple:</b>
<code>/number 0659515481</code>"""
