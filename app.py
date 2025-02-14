from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

def generate_password(length=12):
    """Génère un mot de passe sécurisé avec lettres, chiffres et caractères spéciaux"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    if request.method == "POST":
        try:
            length = int(request.form["length"])
            if length >= 8:
                password = generate_password(length)
            else:
                password = "❌ Minimum 8 caractères !"
        except ValueError:
            password = "❌ Veuillez entrer un nombre valide."
    
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
