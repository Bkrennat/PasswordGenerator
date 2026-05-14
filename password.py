import tkinter as tk
from tkinter import messagebox
import random
import string


def generer_mot_de_passe():
    try:
        longueur = int(entree_longueur.get())
        if longueur < 4:
            messagebox.showwarning("Attention", "Choisis une longueur d'au moins 4 caractères.")
            return
    except ValueError:
        messagebox.showerror("Erreur", "Entre un nombre valide.")
        return

    caracteres = ""

    if var_minuscules.get():
        caracteres += string.ascii_lowercase
    if var_majuscules.get():
        caracteres += string.ascii_uppercase
    if var_chiffres.get():
        caracteres += string.digits
    if var_symboles.get():
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showwarning("Attention", "Sélectionne au moins un type de caractère.")
        return

    mot_de_passe = "".join(random.choice(caracteres) for _ in range(longueur))
    champ_resultat.delete(0, tk.END)
    champ_resultat.insert(0, mot_de_passe)


def copier_mot_de_passe():
    mot_de_passe = champ_resultat.get()

    if mot_de_passe == "":
        messagebox.showwarning("Attention", "Aucun mot de passe à copier.")
        return

    fenetre.clipboard_clear()
    fenetre.clipboard_append(mot_de_passe)
    messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papiers.")


fenetre = tk.Tk()
fenetre.title("Générateur de mot de passe")
fenetre.geometry("420x330")
fenetre.resizable(False, False)

titre = tk.Label(
    fenetre,
    text="Générateur de mot de passe",
    font=("Arial", 18, "bold")
)
titre.pack(pady=15)

cadre_longueur = tk.Frame(fenetre)
cadre_longueur.pack(pady=5)

label_longueur = tk.Label(cadre_longueur, text="Longueur :", font=("Arial", 12))
label_longueur.pack(side=tk.LEFT, padx=5)

entree_longueur = tk.Entry(cadre_longueur, width=10, font=("Arial", 12))
entree_longueur.insert(0, "12")
entree_longueur.pack(side=tk.LEFT)

var_minuscules = tk.BooleanVar(value=True)
var_majuscules = tk.BooleanVar(value=True)
var_chiffres = tk.BooleanVar(value=True)
var_symboles = tk.BooleanVar(value=True)

tk.Checkbutton(fenetre, text="Minuscules", variable=var_minuscules).pack(anchor="w", padx=120)
tk.Checkbutton(fenetre, text="Majuscules", variable=var_majuscules).pack(anchor="w", padx=120)
tk.Checkbutton(fenetre, text="Chiffres", variable=var_chiffres).pack(anchor="w", padx=120)
tk.Checkbutton(fenetre, text="Symboles", variable=var_symboles).pack(anchor="w", padx=120)

bouton_generer = tk.Button(
    fenetre,
    text="Générer",
    font=("Arial", 12, "bold"),
    command=generer_mot_de_passe
)
bouton_generer.pack(pady=15)

champ_resultat = tk.Entry(fenetre, width=35, font=("Arial", 12), justify="center")
champ_resultat.pack(pady=5)

bouton_copier = tk.Button(
    fenetre,
    text="Copier",
    font=("Arial", 11),
    command=copier_mot_de_passe
)
bouton_copier.pack(pady=10)

fenetre.mainloop()
