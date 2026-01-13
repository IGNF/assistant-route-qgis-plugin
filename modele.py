import os

from PyQt5.QtWidgets import QDialog, QLabel, QFrame, QTableWidgetItem, QTextEdit
from PyQt5.uic import loadUi
from qgis.PyQt.QtCore import Qt

CHAMPS_USE = ["nature","nombre_de_voies","largeur_de_chaussee","importance",
              "sens_de_circulation","acces_vehicule_leger","restriction_de_hauteur","restriction_de_largeur",
              "restriction_de_longueur","restriction_de_poids_par_essieu","restriction_de_poids_total"]

def test_modele(layer):
    dico_champ_readonly = {}
    list_champ_manquant = []
    list_champs_modele = []
    for field in layer.fields():
        list_champs_modele.append(field.name())

    for champ in CHAMPS_USE:
        if champ not in list_champs_modele:
            list_champ_manquant.append(champ)
        else:
            if isreadonly(layer,champ):
                dico_champ_readonly[champ] = True
            else:
                dico_champ_readonly[champ] = False
    return list_champ_manquant,dico_champ_readonly

def isreadonly(layer,champ):
    index = layer.fields().indexOf(champ)
    form_config = layer.editFormConfig()
    read_only = form_config.readOnly(index)
    return read_only

def config_modele(champs_manquant,champs_readonly):
    dlgConfig = QDialog()
    loadUi(os.path.join(os.path.dirname(__file__) ,"modele.ui"), dlgConfig)
    dlgConfig.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
    dlgConfig.setWindowTitle("Compatibilité du modéle")

    dlgConfig.tableWidget_etat_champs.setColumnCount(2)
    dlgConfig.tableWidget_etat_champs.setHorizontalHeaderLabels(["Champ", "Lecture/Ecriture"])
    dlgConfig.tableWidget_etat_champs.setRowCount(len(champs_readonly))
    dlgConfig.tableWidget_etat_champs.verticalHeader().setDefaultSectionSize(20)

    # champs manquants
    dlgConfig.textEdit_champs_manquants.setLineWrapMode(QTextEdit.NoWrap)
    for champ in champs_manquant:
        dlgConfig.textEdit_champs_manquants.append(f"<span style = 'color: red'><b>{champ}</b></span>")

    # état des champs
    for row, (champ, readonly) in enumerate(champs_readonly.items()):
        print(champ, readonly)
        if readonly:
            readonly_str = "<span style = 'color: red'><b>NON</b></span>"
        else:
            readonly_str = "OUI"

        label_champ = QLabel(f"{champ}")
        dlgConfig.tableWidget_etat_champs.setCellWidget(row, 0, label_champ)

        label_readonly = QLabel(readonly_str)
        label_readonly.setAlignment(Qt.AlignCenter)
        dlgConfig.tableWidget_etat_champs.setCellWidget(row, 1, label_readonly)

    dlgConfig.tableWidget_etat_champs.resizeColumnsToContents()

    dlgConfig.exec_()