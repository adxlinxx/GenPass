import secrets
import string

def generate_password(length=12):
    """Génère un mot de passe sécurisé avec lettres, chiffres et caractères spéciaux"""
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

# Interface utilisateur
try:
    print("\n🔐 Générateur de mot de passe sécurisé 🔐\n")

    length = int(input("👉 Entrez la longueur du mot de passe (min 8) : "))
    
    if length < 8:
        print("❌ La longueur minimale est de 8 caractères.")
    else:
        password = generate_password(length)
        print("\n✅ Mot de passe généré :", password)

except ValueError:
    print("❌ Erreur : Veuillez entrer un nombre valide.")
