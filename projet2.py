import tkinter as tk
from tkinter import messagebox

# Fonction pour calculer l'IMC
def calculer_imc():
    try:
        taille = float(entry_taille.get())
        poids = float(entry_poids.get())
        imc = poids / (taille ** 2)
        imc = round(imc, 2)

        if imc < 17.0:
            etat = "Vous êtes très mince."
        elif 17.0 <= imc < 18.5:
            etat = "Vous êtes en mince."
        elif 18.5 <= imc < 24.9:
            etat = "Vous avez un poids normal."
        elif 25.0 <= imc < 30.0:
            etat = "Vous êtes en surpoids."
        else:
            etat = "Vous êtes en obésité."

        messagebox.showinfo("Résultat", f"Votre IMC est : {imc}\n{etat}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.geometry('400x400')
fenetre.title("Calculateur d'IMC")
label= tk.Label(fenetre,text="Bienvenu sur mon app de calcul de imc",font=("times news roman",15,"italic"))
label.pack()


# Label et champ pour la taille
label_taille = tk.Label(fenetre, text="Entrez votre taille (en m) :")
label_taille.pack(pady=10)
entry_taille = tk.Entry(fenetre)
entry_taille.pack(pady=10)

# Label et champ pour le poids
label_poids = tk.Label(fenetre, text="Entrez votre poids (en kg) :")
label_poids.pack(pady=10)
entry_poids = tk.Entry(fenetre)
entry_poids.pack(pady=10)

# Bouton pour calculer l'IMC
bouton_calculer = tk.Button(fenetre, text="Calculer IMC", command=calculer_imc)
bouton_calculer.pack(pady=10)

# Boucle principale
fenetre.mainloop()
