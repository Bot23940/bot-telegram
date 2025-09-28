from datetime import datetime

class BotDesign:
    """Classe pour reproduire exactement le design de l'image"""

    @staticmethod
    def format_fiche(fiche_brute, numero):
        try:
            lignes = fiche_brute.split('\n')

            # Extraire les informations
            nom = ""
            date_naissance = ""
            adresse_ligne1 = ""
            adresse_ligne2 = ""
            telephone = ""
            iban = ""
            bic = ""
            email = ""
            ville = ""

            for ligne in lignes:
                ligne_clean = ligne.strip()
                if ligne_clean.startswith('/number'):
                    continue
                elif ligne_clean.startswith('Match found:'):
                    continue
                elif ligne_clean and not any(ligne_clean.startswith(x) for x in ['Né(e)', 'Adresse', 'Téléphone', 'IBAN', 'BIC', 'Email', 'Ville']):
                    nom = ligne_clean
                elif ligne_clean.startswith('Né(e) le'):
                    date_naissance = ligne_clean.split('Né(e) le')[-1].strip()
                elif ligne_clean.startswith('Adresse :'):
                    adresse_ligne1 = ligne_clean.split('Adresse :')[-1].strip()
                elif ligne_clean.startswith('Téléphone(s) :'):
                    telephone = ligne_clean.split('Téléphone(s) :')[-1].strip()
                elif ligne_clean.startswith('IBAN :'):
                    iban = ligne_clean.split('IBAN :')[-1].strip()
                elif ligne_clean.startswith('BIC :'):
                    bic = ligne_clean.split('BIC :')[-1].strip()
                elif ligne_clean.startswith('Email :'):
                    email = ligne_clean.split('Email :')[-1].strip()
                elif ligne_clean.startswith('Ville :'):
                    ville = ligne_clean.split('Ville :')[-1].strip()
                elif ligne_clean and not adresse_ligne2 and adresse_ligne1:
                    # C'est la deuxième ligne de l'adresse
                    adresse_ligne2 = ligne_clean

            # Design exact comme l'image
            return f"""/number {numero}

Match found:

{nom}
Né(e) le {date_naissance}
Adresse : {adresse_ligne1}
{adresse_ligne2}
Téléphone(s) : {telephone}
IBAN :
{iban}
BIC : {bic}
Email :
{email}
Ville : {ville}"""

        except Exception as e:
            return f"❌ Erreur formatage: {e}"

# Exemple d'utilisation
if __name__ == "__main__":
    fiche_exemple = """/number 0659515481

Match found:

Manon LAVERGNE
Né(e) le 19/07/1992
Adresse : 116 BOULEVARD EXELMANS
75016 PARIS
Téléphone(s) : 0659515481
IBAN :
FR80204330262GN265528725335
BIC : NTSBFRM1XXX
Email :
manonlavergne.ml@gmail.com
Ville : PARIS"""

    design = BotDesign()
    resultat = design.format_fiche(fiche_exemple, "0659515481")
    print(resultat)
