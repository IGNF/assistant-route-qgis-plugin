import os.path
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.PyQt.QtCore import Qt

from qgis.core import QgsCoordinateReferenceSystem, QgsProject

import subprocess

from .constante import *


def ecrirelog(text):
    ficlog = open(os.path.dirname(__file__) + "/log.txt", "a")
    ficlog.write(text)
    ficlog.close()
    print("log !!")


def ecrire_debut_fichier(text):
    fic = os.path.dirname(__file__) + "/log.txt"

    text_origine = ""
    if os.path.isfile(fic):
        with open(os.path.dirname(__file__) + "/log.txt", 'r', encoding='utf-8') as file:
            text_origine = file.read()
        with open(os.path.dirname(__file__) + "/log.txt", 'w', encoding='utf-8') as file:
            file.write(text + text_origine)
    else:
        with open(os.path.dirname(__file__) + "/log.txt", 'w', encoding='utf-8') as file:
            file.write(text + text_origine)


def afficheDoc():
    fichier = os.path.join(os.path.dirname(__file__), "contribution directe (route).pdf")
    if not os.path.isfile(fichier):
        afficheerreur("La documentation est introuvable", "Information")
    else:
        subprocess.Popen(['start', '', fichier], shell=True)

def afficherlog():
    fic = os.path.dirname(__file__) + "/transaction.xlsx"

    if not os.path.isfile(fic):
        afficheerreur("Le fichier de log n'existe pas\nIl sera crée dès la premiére transaction", "Information")
    else:
        subprocess.Popen(["start", "excel", fic], shell=True)


def affiches_spec_bdtopo():
    import webbrowser
    webbrowser.open("https://bdtopoexplorer.ign.fr/")


def afficheerreur(text, titre=TITRE_INTERFACE):
    msg = QMessageBox()
    msg.setStyleSheet(FOND_DIAL)
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setText(text)
    msg.setWindowFlags(Qt.WindowStaysOnTopHint)
    msg.exec()


def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setStyleSheet(FOND_DIAL)

    msg.setWindowTitle(titre)
    msg.setText(text)
    btnAnnuler = msg.addButton("Annuler", QMessageBox.YesRole)
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")
    btnValider = msg.addButton("valider les modifications", QMessageBox.AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")
    msg.setWindowFlags(Qt.WindowStaysOnTopHint)
    msg.exec()

    if msg.clickedButton() == btnAnnuler:
        return False
    if msg.clickedButton() == btnValider:
        return True


def list_submenus(menu):
    # Liste pour stocker les sous-menus
    submenus = []
    for action in menu.actions():
        # Vérifie si l'action a un sous-menu
        if action.menu():
            submenus.append(action.menu().title())
            # Récursivement lister les sous-menus
            submenus.extend(list_submenus(action.menu()))
        else:
            submenus.append(action.text())
    return submenus
