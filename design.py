```python
from datetime import datetime

class BotDesign:
    """Classe pour un design avec fond vert et barres verticales collées"""

    @staticmethod
    def format_fiche(fiche_brute, numero):
        try:
            lignes = fiche_brute.split('\n')

            # Extraire le nom
            nom = ""
            for ligne in lignes:
                ligne_clean = ligne.strip()
                if ligne_clean and not ligne_clean.startswith('Né(e)') and not ligne_clean.startswith('Adresse'):
                    nom = ligne_clean
                    break

            # Extraire les infos clé:valeur
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

            for key in infos:
                infos[key] = infos[key].strip()

            heure_actuelle = datetime.now().strftime("%H:%M")

            # Design avec fond vert + barres
            return f"""
<pre>
🟢━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🟢
<b>        ✅ Match found ✅        </b>
🟢━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🟢

👤 {nom}
🗓️ Né(e) le : {infos.get('Né(e) le', 'Non renseigné')}
🏠 Adresse   : {infos.get('Adresse', 'Non renseigné')}
📱 Téléphone : {infos.get('Téléphone(s)', 'Non renseigné')}
💳 IBAN      : {infos.get('IBAN', 'Non renseigné')}
🏦 BIC       : {infos.get('BIC', 'Non renseigné')}
📧 Email     : {infos.get('Email', 'Non renseigné')}
🌆 Ville     : {infos.get('Ville', 'Non renseigné')}

⏰ {heure_actuelle}
🟢━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🟢
</pre>
"""
        except Exception as e:
            return f"❌ Erreur formatage: {e}"
```
